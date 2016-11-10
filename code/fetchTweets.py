from TwitterSearch import *

def fetchTweet(searchterm) :
	try:
		deleteWords = ['sleeve', 'giveaway', 'takeaway', 'website', 'ebay', 'amazon', 'buy', 'sale']
		ts = TwitterSearch (
			consumer_key = 'qnDfVfsAf73E7Bxyf9kVRWTVg',
			consumer_secret = 'danStpX5V2vbHXz2uBdWEcFpEXnUdbG2jlUwU7Xd37YHJa1xWQ',
			access_token = '17994241-c2dim0Wxxjr43n4jzot7w9gkhg9mA3cz92h1uuAf7',
			access_token_secret = 'OimBGv92bHaTOBMozMGttKICTBktG8JCi5ZQN6z4IFHLZ'
		)
		
		tso = TwitterSearchOrder()
		tso.set_keywords([searchterm])
		tso.set_language('en')
		tso.set_include_entities(True)

		tweets = []
		for tweet in ts.search_tweets_iterable(tso):
			wordsInTweet = tweet['text'].split(' ')
			for word in wordsInTweet :
				if word in deleteWords :
					continue
			tweets.append(tweet)
		return tweets
	except TwitterSearchException as e:
	    return None

if __name__ == '__main__':
	keywords = ['#iphone7', '#iphone7plus', '#iphone6s', '#iphone6splus', '#iphone6', '#iphone6plus', '#galaxys7', '#lgg5', '#googlepixel', '#googlepixelxl']
	op = open('tweets.json', 'w')
	for keyword in keywords :
		op.write(keyword)
		op.write(fetchTweet(keyword))
		op.write('\n\n')

