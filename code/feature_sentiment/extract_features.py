from __future__ import division

import pandas as pd
import numpy as np

def get_reviews_for_phone(data):
	return data.values()


def extract_aspects(reviews):
	from extract_aspects import get_sentences, tokenize, pos_tag, aspects_from_tagged_sents

	sentences = []
	for review in reviews :
			sentences.extend(get_sentences(review))
	tokenized_sentences = [tokenize(sentence) for sentence in sentences]
	tagged_sentences = [pos_tag(sentence) for sentence in tokenized_sentences]

	aspects = all_aspects_from_tagged_sents(tagged_sentences)

	return aspects


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

	import os

	DATAPATH = os.getcwd()
	DATAPATH = DATAPATH + os.sep + "feature" + os.sep + "features_"

	features = set()
	for phone in phones:
		output_file = open(DATAPATH + phone + ".txt", "w")
		data = read_data(phone)
		reviews = get_reviews_for_phone(data)
		f = extract_aspects(reviews)
		for k in f :
			output_file.write(k.encode("utf-8") + "\n")

if __name__ == "__main__":
	main()
