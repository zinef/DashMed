import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .dataloader import dataloader
from .preprocessor import preprocessor
from .vectorizer import vectorizer
from .parser import parser

tfidf_vector = vectorizer.vectorize(method='tfidf')    
tfidf_df = vectorizer.to_df()
my_vectorizer,X = vectorizer.get_params()



def get_sims(desc,df,vectorizer,size=5):
    processed_desc = preprocessor.preprocessing(desc)
    tf_desc = vectorizer.transform([processed_desc])
    values = sorted(cosine_similarity(df.values,tf_desc).flatten())[-size:][::-1]
    idxs = df.iloc[cosine_similarity(df.values,tf_desc).flatten().argsort()[-size:][::-1]].index
    ratios = values / values[0]
    return sorted(list(zip(idxs,values,ratios)),key= lambda x: x[1],reverse=True)

def get_best_articles(desc , size=5):
    df = tfidf_df.copy()
    best_articles = get_sims(desc,df,my_vectorizer,size)
    processed_desc = preprocessor.preprocessing(desc)
    v_processed_desc = my_vectorizer.transform([processed_desc]).toarray()[0]
    desc_tokens = pd.Series(v_processed_desc,index=my_vectorizer.get_feature_names_out())
    res = []

    for idx,sim, ratio in best_articles : 
        article = df.iloc[idx, : ]
        token_res = desc_tokens[desc_tokens.astype(bool) & article.astype(bool).nlargest()]
        tokens  = [tok.capitalize() for tok in token_res.index]
        values = [val for val in token_res.values]
        values /=  sum(values) + np.finfo(float).tiny
        token_final = list(zip(tokens,values))
        res.append({
            'article':idx,
            'Title':parser.parse_article(dataloader.articles[idx])['ArticleTitle'] ,
            'sim': sim,
            'ratio': ratio,
            'tokens': token_final
        })

    return res