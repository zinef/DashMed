from DashMed.dataloader import dataloader
from DashMed.vectorizer import vectorizer
# import pickle
# infile = open('corpus','rb')
# corpus_list = pickle.load(infile)
# print(corpus_list[0])
# infile.close()

vectorizer.vectorize()
vectorizer,X = vectorizer.get_params()

