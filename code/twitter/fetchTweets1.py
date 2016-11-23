
import os
import json

from twitter import Api

api = Api(consumer_key = '',
	consumer_secret = '',
	access_token_key = '',
	access_token_secret = ''
)

filter1 = ['#iphone7', '#iphone6s', '#iphone6splus', '#googlepixel', '#pixel', '#iphone6', '#iphone6plus', '#galaxys7', '#lgg5', '#pixel', '#samsungs7', '#iphone7plus']


if __name__ == '__main__':
	f = open("tweets.txt", "a")
	for line in api.GetStreamFilter(track=filter1):
		 print str(line['id']) + "," + line['text'].encode('utf-8') + "\n"
	keywords = ['#iphone7']#, '#iphone7plus', '#iphone6s', '#iphone6splus', '#iphone6', '#iphone6plus', '#galaxys7', '#lgg5', '#googlepixel', '#googlepixelxl']
	

