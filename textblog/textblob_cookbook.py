import os
import re

import mysql.connector
from mysql.connector import Error

import pandas as pd
import numpy as np  

from textblob import TextBlob

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

class TweetObject():

    def __init__(self, host, database, user):
        self.password = os.environ['PASSWORD']
        self.host = host
        self.database = database
        self.user = user
    

    def MySQLConnect(self, query):





