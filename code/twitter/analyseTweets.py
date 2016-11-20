from __future__ import division
from nltk.corpus import wordnet

import pandas as pd
import numpy as np
import os

def read_feaures_csv() :
    DATAPATH = os.getcwd()
    DATAPATH = DATAPATH + os.sep + "all_features.txt"

    csv = open(DATAPATH, "r")
    features = []
    for line in csv :
        features.append(line.split("\r")[0].split("\n")[0])
    return features


def get_relevant_aspects(tweet_aspects, aspects) :
    import itertools

    new_tweet_aspects = []
    syns1 = {}
    for w in tweet_aspects :
        w = w.strip()
        if "#" in w :
            w = w.split("#")[1]
        if len(w) > 0:
            syns1[w] = wordnet.synsets(w)
            new_tweet_aspects.append(w)

    syns2 = {}
    for w in aspects :
        w = w.strip()
        if len(w) > 0 :
            syns2[w] = wordnet.synsets(w)

    words = list(itertools.product(new_tweet_aspects, aspects))

    similarity_scores = {}
    for pair in words :
        try :
            s1 = syns1[pair[0]]
            s2 = syns2[pair[1]]
            if s1 and s2 :
                s =  s1[0].wup_similarity(s2[0])
                if s > 0.7:
                    if pair[0] in similarity_scores :
                        similarity_scores[pair[0]].append(pair[1])
                    else :
                        similarity_scores[pair[0]] = [pair[1]]
        except :
            pass

    return similarity_scores


def get_tweets() :
    DATAPATH = os.getcwd()
    DATAPATH = DATAPATH + os.sep + "tweets.txt"
    tweet_file = open(DATAPATH)

    phones = {'#iphone7' : 'iphone7', '#iphone6s' : 'iphone_6s', '#iphone6splus': 'iphone_6s', '#googlepixel' : 'pixel'}
    phones.update({'#pixel' : 'pixel', '#iphone6' : 'iphone_6', '#iphone6plus' : 'iphone_6plus', '#galaxys7' : 'galaxy_s7'})
    phones.update({'#lgg5' : 'lg_g5', '#samsungs7' : 'galaxy_s7', '#iphone7plus' : 'iphone7'})

    hash_tags = phones.keys()
    unique_phones = phones.values()

    tweets = {}
    for phone in unique_phones :
        tweets[phone] = {}

    deleteWords = ['sleeve', 'giveaway', 'takeaway', 'website', 'ebay', 'amazon', 'buy', 'sale', '#giveaway', 'contest', 'wallpapers', 'inkcase', 'case']

    for tweet in tweet_file :
        contents = tweet.split(",")
        tweet_id = contents[0]
        tweet_text = ", ".join(contents[1:])

        words_in_tweet = tweet_text.split(" ")
        phone = None
        save = True

        for word in words_in_tweet :
            if word in hash_tags :
                phone = phones[word]
            if word in deleteWords :
                save = False
        if phone is not None and save :
            tweets[phone][tweet_id] = tweet_text
    return tweets


def extract_aspects(tokenized_tweet):
    from extract_aspects import pos_tag, all_aspects_from_tagged_sents

    tagged_sentence = pos_tag(tokenized_tweet)
    aspects = all_aspects_from_tagged_sents(tagged_sentence)
    return aspects


def score_aspect(aspect_sentences):
	from score_aspect import SentimentScorer, get_sentences_by_aspect

	sentiment_scorer = SentimentScorer()
	scores = [sentiment_scorer.score(sent) for sent in aspect_sentences]

	return np.mean(scores)


def aspect_opinions(tweets, aspects):
    from extract_aspects import get_sentences, tokenize, pos_tag, aspects_from_tagged_sents

    sentences = []
    for tweet in tweets :
            sentences.extend(get_sentences(tweets[tweet]))
    tokenized_sentences = [tokenize(sentence) for sentence in sentences]

    aspect_to_tweets = {}

    for tweet in tokenized_sentences :
        tweet_aspects = extract_aspects(tweet)
        relevant_aspects = get_relevant_aspects(tweet_aspects, aspects)
        for p_aspect in relevant_aspects :
            #value has the relevant aspects. create a dictionary and push the tweets
            p_aspects = relevant_aspects[p_aspect]
            for aspect in p_aspects :
                if aspect in aspect_to_tweets :
                    aspect_to_tweets[aspect].append(tweet)
                else :
                    aspect_to_tweets[aspect] = []
                    aspect_to_tweets[aspect].append(tweet)
    features = {}
    for aspect, tweets in aspect_to_tweets.items() :
        features[aspect] = [len(tweets), score_aspect(tweets)]
    return features

def main():
    aspects = read_feaures_csv()
    tweets = get_tweets()
    phones = ['iphone_6', 'iphone_6plus', 'iphone_6s', 'iphone7', 'lg_g5', 'pixel', 'galaxy_s7']
    phone_features = {}
    for phone in phones :
        phone_features[phone] = aspect_opinions(tweets[phone], aspects)
        print phone
        print phone_features[phone]
        print "\n\n"

if __name__ == "__main__":
	main()
