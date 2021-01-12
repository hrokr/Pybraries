import os
import re

import pandas as pd
import numpy as np 

import mysql.connector
from mysql.connector import Error

import tweepy
from textblob import TextBlob

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

#from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

api_key = os.

auth = tweepy.OAuthHandler(api_key, api_secret)
#auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)

class TweetObject():

    def __init__(self, host, database, user):
        self.password = os.environ['PASSWORD']
        self.host = host
        self.database = database
        self.user = user
    

    def MySQLConnect(self, query):
        pass





