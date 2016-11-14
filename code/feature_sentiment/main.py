from __future__ import division

import pandas as pd
import numpy as np

def get_reviews_for_phone(data):
	"""
	INPUT: data dictionary. {filename : data}
	OUTPUT: dataframe of the reviews
	"""
	return data.values()


def extract_aspects(reviews):
	"""
	INPUT: iterable of strings (pd Series, list)
	OUTPUT: list of aspects

	Return the aspects from the set of reviews
	"""

	# import the aspect extraction functions
	from extract_aspects import get_sentences, tokenize, pos_tag, aspects_from_tagged_sents

	# put all the sentences in all reviews in one stream
	#sentences = []
	#for review in reviews:
	#	sentences.extend(get_sentences(review))
	sentences = []
	for review in reviews :
			sentences.extend(get_sentences(review))

	tokenized_sentences = [tokenize(sentence) for sentence in sentences]

	# tokenize each sentence
	#tokenized_sentences = [tokenize(sentence) for sentence in sentences]

	# pos tag each sentence
	tagged_sentences = [pos_tag(sentence) for sentence in tokenized_sentences]

	# from the pos tagged sentences, get a list of aspects
	aspects = aspects_from_tagged_sents(tagged_sentences)

	return aspects


def score_aspect(reviews, aspect):
	"""
	INPUT: iterable of reviews, iterable of aspects
	OUTPUT: score of aspect on given set of reviews

	For a set of reviews and corresponding aspects,
	return the score of the aspect on the reviews
	"""

	from score_aspect import SentimentScorer, get_sentences_by_aspect

	sentiment_scorer = SentimentScorer()
	aspect_sentences = get_sentences_by_aspect(aspect, reviews)
	scores = [sentiment_scorer.score(sent) for sent in aspect_sentences]

	return np.mean(scores)


def aspect_opinions(reviews):
	"""
	INPUT: a set of reviews
	OUTPUT: dictionary with aspects as keys and values as scores
	"""

	aspects = extract_aspects(reviews)
	return dict([(aspect, score_aspect(reviews, aspect)) for aspect in aspects])


def read_data(phone):
	"""
	INPUT: phone name
	OUTPUT: dictionary of filename, text
	"""

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
	score = {}

	for phone in phones:
		data = read_data(phone)

		reviews = get_reviews_for_phone(data)
		score[phone] = aspect_opinions(reviews)
		print phone + " done"
	print score
if __name__ == "__main__":
	main()
