import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from unidecode import unidecode
import re

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


class Preprocessor:

    
    def __init__(self) -> None:
        self.stops = set(stopwords.words('english'))


    def preprocessing(self, text ):
        #lower
        data = text.lower()

        #Noise removal
        data = re.sub(r'https?://[^\s\n\r]+',' ',data)
        data = re.sub(r'\.|\!|\"|\?|\-|\,|\:|\+|\(|\)|\&|\/|\<|\>',' ',data)
        data = re.sub(r'\d+',' ',data)
        data=data.strip()

        data_clean = []
        #stopwords -> /dev/null & tokenize
        data_clean  = [
            unidecode(word.lower()) for word in data.split() if word.lower() not in self.stops
        ]

        data_lemmatized = []
        #stemming or lemmatization
        wordnet_lemmatizer = WordNetLemmatizer()
        for w in data_clean:
            data_lemmatized.append(wordnet_lemmatizer.lemmatize(w))

        res = list(set(data_lemmatized))
        return ' '.join(res)


preprocessor = Preprocessor()

# s="On the contrary, Lemmatization is a more powerful operation, and it takes into consideration morphological analysis of the words."
# print(preprocessor.preprocessing(s))