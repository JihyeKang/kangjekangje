#-*- coding: utf-8 -*-a
from flask import Flask, request, render_template
from urllib import urlopen
from bs4 import BeautifulSoup
import tweepy
import json

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('main.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

@app.route('/webtoon')
def webtoon():
	data = urlopen('http://comics.nate.com/webtoon/detail.php?btno=64923')
	soup = BeautifulSoup(data)
	img_div = soup.find('div', {"class":"toonView"})
	img = img_div.findAll('img')
	return render_template("webtoon.html", img = img)

@app.route('/searchtwit', methods=['GET','POST'])
def searchtwit():
	if request.method == 'POST' :
		consumer_key='Ka13T0ZyJ1HRzHYzbGK29jhKn'
		consumer_secret='X1tOUbBpbH9qAvQpHhO4wZBIhCueF6o8fwTD4Sl819t33tOeNY'
		access_token='2687254046-k7tCpMnDAGWbB6XN17kovqRHZcVAYp4bF9UW5uX'
		access_token_secret='Wv2eNUOc1TDfKdBST9SkRrhDYcIGj4TpVNQIWFBQTvxSE'

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		twit_list=[]
		api = tweepy.API(auth)
		text = request.form['text']
		search_results = api.search(q=text, count=10)
		for result in search_results:
			temp={
			"text":result.text,
			"user":result.user.screen_name
			}
			twit_list.append(temp)
		return json.dumps(twit_list)
	else:
		return render_template("searchtwit.html")


