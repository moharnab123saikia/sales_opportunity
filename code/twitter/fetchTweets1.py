
import os
import json

from twitter import Api

api = Api(consumer_key = 'qnDfVfsAf73E7Bxyf9kVRWTVg',
	consumer_secret = 'danStpX5V2vbHXz2uBdWEcFpEXnUdbG2jlUwU7Xd37YHJa1xWQ',
	access_token_key = '17994241-c2dim0Wxxjr43n4jzot7w9gkhg9mA3cz92h1uuAf7',
	access_token_secret = 'OimBGv92bHaTOBMozMGttKICTBktG8JCi5ZQN6z4IFHLZ'
)

filter1 = ['#iphone7', '#iphone6s', '#iphone6splus', '#googlepixel', '#pixel', '#iphone6', '#iphone6plus', '#galaxys7', '#lgg5', '#pixel', '#samsungs7', '#iphone7plus']


if __name__ == '__main__':
	f = open("tweets.txt", "a")
	for line in api.GetStreamFilter(track=filter1):
		 print str(line['id']) + "," + line['text'].encode('utf-8') + "\n"
	keywords = ['#iphone7']#, '#iphone7plus', '#iphone6s', '#iphone6splus', '#iphone6', '#iphone6plus', '#galaxys7', '#lgg5', '#googlepixel', '#googlepixelxl']
	

