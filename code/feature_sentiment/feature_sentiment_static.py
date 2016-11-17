from __future__ import division

import pandas as pd
import numpy as np

def get_relevant_features() :
	import os

	DATAPATH = os.getcwd()
	DATAPATH = os.sep.join(DATAPATH.split(os.sep))
	DATAPATH += os.sep + "feature" + os.sep + "relevant_features.csv"

	f = open(DATAPATH, "r")
	features = {}
	for line in f :
		if len(line) > 0:
			contents = line.split(",")
			features[contents[0]] = contents[1].split("\r\n")[0]
	return features

def get_reviews_for_phone(phone):
	data = read_data(phone)
	return data.values()


def extract_aspects(phone):
	aspects = {}

	import os

	DATAPATH = os.getcwd()
	DATAPATH = os.sep.join(DATAPATH.split(os.sep))
	DATAPATH += os.sep + "feature" + os.sep + "relevant_features_" + phone + ".csv"

	f = open(DATAPATH, "r")
	for line in f :
		if len(line) > 0 :
			line = line [: -1]
			content = line.split(",")
			aspects[content[0]] = content[1]
	return aspects


def score_aspect(tokenized_sentences, aspect):
	from score_aspect import SentimentScorer, get_sentences_by_aspect

	sentiment_scorer = SentimentScorer()
	aspect_sentences = get_sentences_by_aspect(aspect, tokenized_sentences)
	if len(aspect_sentences) == 0 :
		return 0
	scores = [sentiment_scorer.score(sent) for sent in aspect_sentences]
	return (len(aspect_sentences), np.mean(scores))


def aspect_opinions(reviews, aspects, relevant_features):

	from extract_aspects import get_sentences, tokenize, pos_tag, aspects_from_tagged_sents

	sentences = []
	for review in reviews :
			sentences.extend(get_sentences(review))

	tokenized_sentences = [tokenize(sentence) for sentence in sentences]
	scores = [(aspect[1], score_aspect(tokenized_sentences, aspect[0])) for aspect in aspects.items()]

	aspect_scores = {}
	for score in scores :
		klass = relevant_features[score[0]]
		if klass in aspect_scores :
			old_count = aspect_scores[klass][0]
			old_score = aspect_scores[klass][1]
			new_count = old_count + score[1][0]
			new_score = ( old_count * old_score + new_count * score[1][1] ) / (old_count + new_count)
			aspect_scores[klass] = (new_count, new_score)
		else :
			aspect_scores[klass] = (score[1][0], score[1][1])

	return aspect_scores


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
	"""
	The true main.
	"""
	phones = ['iphone_6', 'iphone_6plus', 'iphone_6s', 'iphone7', 'lg_g5', 'pixel', 'galaxy_s7']
	#phones = ['iphone_6']
	relevant_features = get_relevant_features()

	feature_scores = {}
	for phone in phones:
		reviews = get_reviews_for_phone(phone)
		aspects = extract_aspects(phone)
		feature_scores[phone] = aspect_opinions(reviews, aspects, relevant_features)
		print phone
		print feature_scores[phone]
		print "\n\n"
	return feature_scores

if __name__ == "__main__":
	import sys
	main()
