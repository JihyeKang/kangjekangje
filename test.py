#-*- coding: utf-8 -*-a
import appengine_config
from flask import Flask, render_template
from urllib import urlopen
from bs4 import BeautifulSoup
import tweepy
import json

app = Flask(__name__)
app.config['DEBUG'] = True

consumer_key='Ka13T0ZyJ1HRzHYzbGK29jhKn'
consumer_secret='X1tOUbBpbH9qAvQpHhO4wZBIhCueF6o8fwTD4Sl819t33tOeNY'
access_token='2687254046-k7tCpMnDAGWbB6XN17kovqRHZcVAYp4bF9UW5uX'
access_token_secret='Wv2eNUOc1TDfKdBST9SkRrhDYcIGj4TpVNQIWFBQTvxSE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
search_results = api.search(q="날씨", count=10)
twit_list=[]
for result in search_results:
	temp={
	"text":result.text,
	"user":result.user.screen_name
	}
	twit_list.append(temp)
print twit_list

print json.dumps(twit_list)