from TwitterSearch import *

def fetchTweet(searchterm) :
	try:
		deleteWords = ['sleeve', 'giveaway', 'takeaway', 'website', 'ebay', 'amazon', 'buy', 'sale', '#giveaway', 'contest', 'wallpapers', 'inkcase', 'case']
		ts = TwitterSearch (
			consumer_key = '',
			consumer_secret = '',
			access_token = '',
			access_token_secret = ''
		)

		tso = TwitterSearchOrder()
		tso.set_keywords([searchterm])
		tso.set_language('en')
		tso.set_include_entities(False)

		tweets = []
		for tweet in ts.search_tweets_iterable(tso):
			wordsInTweet = tweet['text'].split(' ')
			includeT = True
			for word in wordsInTweet :
				for dword in  deleteWords :
					if dword in word.lower() :
						includeT = False
						break
			if includeT :
				tweets.append(tweet['text'].encode('utf-8'))
		return tweets
	except TwitterSearchException as e:
	    return []

if __name__ == '__main__':
	keywords = ['#iphone7', '#iphone7plus', '#iphone6s', '#iphone6splus', '#iphone6', '#iphone6plus', '#galaxys7', '#lgg5', '#googlepixel',]
	op = open('/home/vivek/Desktop/sales_opportunity/code/tweets1.json', 'a')
	for keyword in keywords :
		op.write(keyword)
		tweets = fetchTweet(keyword)
		for tweet in tweets :
			op.write(tweet + "\n")
		op.write('\n\n')
