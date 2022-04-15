import os
import io
import json
from unidecode import unidecode
from Bio import Entrez
from .preprocessor import preprocessor
from .parser import parser
import pickle 

MAIL="zine-eddine.fodil@etu.u-paris.fr"
W_DIR = os.path.dirname(os.path.abspath(__file__))


class Dataloader:

    WORDS_DIR = os.path.join(W_DIR,'resources','words')

    def __init__(self, queries_file = os.path.join(WORDS_DIR,'queries.txt')) -> None:
        self.queries = self.get_words(queries_file)
        self.fetch_data(mail=MAIL)

    def get_words(self,path):
        print(path)
        lines = []
        try:
            with io.open(path,mode = 'r', encoding='utf-8') as f : 
                lines = f.readlines()
                lines = [ unidecode(elt.strip().lower()) for elt in lines if elt.strip()]
                return lines
        except Exception as ex: 
            print(f'Error when reading file {path}')
            raise ex

    def search(self,query,mail=MAIL):
        Entrez.email = mail
        handle = Entrez.esearch(db='pubmed',
                                sort='relevance',
                                retmax='20',
                                retmode='xml',
                                term=query)
        results = Entrez.read(handle)
        return results

    def fetch_details(self,id_list,mail=MAIL):
        ids = ','.join(id_list)
        Entrez.email = mail
        handle = Entrez.efetch(db='pubmed',
                            retmode='xml',
                            id=ids)
        results = Entrez.read(handle)
        return results

    def list_relevance_articles(self,query):
        results = self.search(query)
        id_list = results['IdList']
        papers = self.fetch_details(id_list)
        for i, paper in enumerate(papers['PubmedArticle']):
            print("{}) {}".format(i+1, paper['MedlineCitation']['Article']['ArticleTitle']))

        #call print_paper to print a specific paper 
        paper = papers['PubmedArticle'][0]
        self.print_paper(paper)

    def print_paper(self,paper):
        print(json.dumps(paper, indent=2))

    def fetch_data(self,mail):
        self.err = []
        self.articles = []
        self.corpus = []
        
        for query in self.queries :
            try : 
                results = self.search(query)
                id_list = results['IdList']
                papers = self.fetch_details(id_list)
                for i, paper in enumerate(papers['PubmedArticle']):
                    #print("{}) {}".format(i+1, paper['MedlineCitation']['Article']['ArticleTitle']))
                    self.articles.append(paper)
                    self.corpus.append(
                        preprocessor.preprocessing(
                            parser.extract_parsed_article_text(paper)
                        )
                    )

            except Exception as e:
                print(e)
                self.err.append(query)

        #serialize all the data 
        outfile_corpus = open('corpus','wb')
        pickle.dump(self.corpus,outfile_corpus)
        outfile_corpus.close()

        outfile_articles = open('articles','wb')
        pickle.dump(self.articles,outfile_articles)
        outfile_articles.close()





dataloader= Dataloader()
