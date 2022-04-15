import numpy as np
import pandas as pd
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .dataloader import dataloader
from .preprocessor import preprocessor


class Vectorizer:

    def __init__(self) -> None:
        self.vectorizer = None
        self.X = None

    def vectorize(self,method='tfidf',corpus=dataloader.corpus,stopwords=preprocessor.stops):
        if method == 'tfidf':
            vectorizer = TfidfVectorizer()
            vectorizer = TfidfVectorizer(stop_words=stopwords)
            tfidf_vector = vectorizer.fit_transform(corpus)

            self.vectorizer = vectorizer
            self.X = tfidf_vector
        elif method == 'tf':
            vectorizer = CountVectorizer()
            vectorizer = CountVectorizer(stop_words=stopwords)
            tf_vector = vectorizer.fit_transform(corpus)

            self.vectorizer = vectorizer
            self.X = tf_vector
        else :
            print('Method not provided.')
    
    def get_params(self):
        return self.vectorizer,self.X

    def to_df(self):
        tfidf_df  = pd.DataFrame(self.X.toarray(),columns=self.vectorizer.get_feature_names_out())
        return tfidf_df

vectorizer  = Vectorizer()