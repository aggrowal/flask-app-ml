from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfTransformer ,CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
import re
from nltk.stem import WordNetLemmatizer
import joblib

class predict_jihad:
    def __init__(self):
        super().__init__()
        lemmatizer = WordNetLemmatizer()
        file = './filename_v2.pkl'
    def deserialize(self):
        model = joblib.load(open('filename_v2.pkl','rb'))
        return model

    def get_prediction(self,text):
        model = self.deserialize()
        return model.predict_proba([text])[0][1]