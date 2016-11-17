from __future__ import division

import pandas as pd
import numpy as np

def get_tweets() :
    DATAPATH = os.getcwd()
	DATAPATH = DATAPATH + os.sep + "tweets.txt"
    tweet_file = open(DATAPATH)
    phones = {'#iphone7' : 'iphone7', '#iphone6s' : 'iphone_6s', '#iphone6splus': 'iphone_6s', '#googlepixel' : 'pixel', '#pixel' : 'pixel', '#iphone6' : 'iphone_6', '#iphone6plus' : 'iphone_6plus', '#galaxys7' : 'galaxy_s7', '#lgg5' : 'lg_g5', '#samsungs7' : galaxy_s7, '#iphone7plus' : 'iphone7']
    hash_tags = phones.keys()
    unique_phones = phones.values()

    tweets = {}
    for phone in unique_phones :
        tweets[phone] = {}

    for tweet in tweet_file :
        contents = tweet.split(",")
        tweet_id = contents[0]
        tweet_text = ", ".join(contents[1:])

        words_in_tweet = tweet_text.split(" ")
        for word in words_in_tweet :
            if word in hash_tags :
                phone = phones[word]
                tweets[phone][tweet_id] = tweet_text

    return tweets

def extract_aspects(tokenized_tweets):
	tagged_sentences = [pos_tag(sentence) for sentence in tokenized_sentences]
	aspects = aspects_from_tagged_sents(tagged_sentences)
	return aspects


def score_aspect(tokenized_tweets, aspect):
	from score_aspect import SentimentScorer, get_sentences_by_aspect

    tweet_contents = tweets.values()

	sentiment_scorer = SentimentScorer()
	aspect_sentences = get_sentences_by_aspect(aspect, reviews)
	scores = [sentiment_scorer.score(sent) for sent in aspect_sentences]

	return np.mean(scores)


def aspect_opinions(reviews):
    from extract_aspects import get_sentences, tokenize, pos_tag, aspects_from_tagged_sents

	sentences = []
	for review in reviews :
			sentences.extend(get_sentences(review))

	tokenized_sentences = [tokenize(sentence) for sentence in sentences]
	return dict([(aspect, score_aspect(tokenized_sentences, aspect)) for aspect in aspects])

	aspects = extract_aspects(reviews)
	return aspects

def main():
    tweets = get_tweets()
    phones = ['iphone_6', 'iphone_6plus', 'iphone_6s', 'iphone7', 'lg_g5', 'pixel', 'galaxy_s7']

    for phone in phones :
        phone_features = aspect_opinions(tweets[phone])


if __name__ == "__main__":
	main()
