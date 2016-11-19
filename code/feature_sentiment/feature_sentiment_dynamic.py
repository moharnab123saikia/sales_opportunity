from __future__ import division

import pandas as pd
import numpy as np

def get_reviews_for_phone(phone):
	data = read_data(phone)
	return data.values()


def extract_aspects():
	aspects = []

	import os

	DATAPATH = os.getcwd() + os.sep + "dynamic_features.txt"

	f = open(DATAPATH)
	for line in f :
		if len(line) > 0 :
			aspects.append(line[:-1])
	return aspects


def score_aspect(tokenized_sentences, aspect):
	from score_aspect import SentimentScorer, get_sentences_by_aspect

	sentiment_scorer = SentimentScorer()
	aspect_sentences = get_sentences_by_aspect(aspect, tokenized_sentences)
	if len(aspect_sentences) == 0 :
		return 0
	scores = [sentiment_scorer.score(sent) for sent in aspect_sentences]
	return (len(aspect_sentences), np.mean(scores))


def aspect_opinions(reviews, aspects):

	from extract_aspects import get_sentences, tokenize, pos_tag, aspects_from_tagged_sents

	sentences = []
	for review in reviews :
			sentences.extend(get_sentences(review))

	tokenized_sentences = [tokenize(sentence) for sentence in sentences]
	return dict([(aspect, score_aspect(tokenized_sentences, aspect)) for aspect in aspects])


def read_data(phone):
	import os
	from os import listdir
	from os.path import isfile, join

	DATAPATH = os.getcwd()
	DATAPATH = os.sep.join(DATAPATH.split(os.sep)[:-2])
	DATAPATH = DATAPATH + os.sep + "lexis_nexis_data" + os.sep + phone + os.sep + "output"
	filenames = [DATAPATH + os.sep + f for f in listdir(DATAPATH) if isfile(join(DATAPATH, f))]

	data = {}
	for f in filenames :
		inputfile = open(f , "r")
		data[f] = inputfile.read()
	return data

def main():
	phones = ['iphone_6', 'iphone_6plus', 'iphone_6s', 'iphone7', 'lg_g5', 'pixel', 'galaxy_s7']

	aspects = extract_aspects()
	feature_scores = {}
	for phone in phones:
		reviews = get_reviews_for_phone(phone)
		feature_scores[phone] = aspect_opinions(reviews, aspects)
		print phone
		print feature_scores[phone]
		print "\n\n"
	return feature_scores

if __name__ == "__main__":
	main()
