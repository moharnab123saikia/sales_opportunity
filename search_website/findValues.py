import random
#read the sentiments, counts, twitter sentiments, counts
# find their headers

def read_all_features() :
    import os
    DATAPATH = "/home/vivek/Desktop/sales_opportunity/code/all_features.csv"

    features = {}
    _file = open(DATAPATH, "r")
    for line in _file :
        content = line.split(",")
        features[content[0]] = content[1].split("\r")[0].split("\n")[0]
    return features


def get_phone_features() :
	specs = open('/home/vivek/Desktop/sales_opportunity/code/phone_features.csv', 'r')
	feature_headers = []
	lno = 0
	specifications = {}
	for line in specs :
		if lno == 0 :
			feature_headers = line.split('\n')[0].split(',')
		else :
			vals = line.split('\n')[0].split(',')
			l = None
			for i,v in enumerate(vals):
				if i == 0 :
					specifications[v] = {}
					l = v
				else :
					specifications[l][feature_headers[i]] = v
		lno += 1
	return specifications
	
def extract_dictionaries(inputfile):
	lineno = 0
	features = set()
	feature_s = []
	sentiment = {}
	phone = None
	for line in inputfile :
		if len(line) > 0: 
			fs = line.split("\n")[0].split(",")
			if lineno == 0 :
				for f in fs:
					if f != "phones" :
						features.add(f)
						feature_s.append(f)
			else :
				l = 0
				for f in fs:
					if l == 0:
						sentiment[f] = {}
						phone = f
					else :
						sentiment[phone][feature_s[l-1]] = f
					l += 1
			lineno += 1
	return features, sentiment

def get_top_values(exp_price, features_input) :
	sentiments_csv = open('/home/vivek/Desktop/sales_opportunity/code/sentiments.csv', 'r')
	twitter_sentiments_csv = open('/home/vivek/Desktop/sales_opportunity/code/twitter_sentiments.csv', 'r')
	counts_csv = open('/home/vivek/Desktop/sales_opportunity/code/counts.csv', 'r')
	twitter_counts_csv = open('/home/vivek/Desktop/sales_opportunity/code/twitter_counts.csv', 'r')
	ln_f, ln_sentiments = extract_dictionaries(sentiments_csv)
	ln_f1, ln_counts = extract_dictionaries(counts_csv)

	#t_f, t_sentiments = extract_dictionaries(twitter_sentiments_csv)
	#t_f1, t_counts = extract_dictionaries(twitter_counts_csv)

	features = ln_f
	for f in ln_f1 :
		features.add(f)
	#for f in t_f :
	#	features.add(f)
	#for f in t_f1 :
	#	features.add(f)
	
	specifications = get_phone_features()
	phones = specifications.keys()
	
	unwanted_phones = []

	all_features = read_all_features()
	
	for phone in specifications :
		phone_price = int(specifications[phone]['price'])
		if phone_price > exp_price + 50 or phone_price < exp_price - 50 :
			unwanted_phones.append(phone)
	
	
	for p in unwanted_phones :
		phones.remove(p)
	
	feature_phones = {}
	
	phone_names = {}
	for phone in phones :
		phone_names[phone] = specifications[phone]['phone']

	for feature in features_input :
		max_sentiment = 0
		max_senti_phone = None
		feature = all_features[feature]
		for phone in phones :
			if max_senti_phone is None :
				max_senti_phone = phone
				max_sentiment = ln_sentiments[phone_names[phone]][feature]
			elif ln_sentiments[phone_names[phone]][feature] > max_sentiment :
				max_sentiment = ln_sentiments[phone_names[phone]][feature]
				max_senti_phone = phone
		feature_phones[feature] = max_senti_phone
	
	v = {}
	for feature in features_input :
		feature1 = all_features[feature]
		phid = feature_phones[feature1]
		v[feature] = specifications[phid][feature]
	
	return v
	
	
def get_random_values(exp_price, features_input) :
	sentiments_csv = open('/home/vivek/Desktop/sales_opportunity/code/sentiments.csv', 'r')
	twitter_sentiments_csv = open('/home/vivek/Desktop/sales_opportunity/code/twitter_sentiments.csv', 'r')
	counts_csv = open('/home/vivek/Desktop/sales_opportunity/code/counts.csv', 'r')
	twitter_counts_csv = open('/home/vivek/Desktop/sales_opportunity/code/twitter_counts.csv', 'r')
	ln_f, ln_sentiments = extract_dictionaries(sentiments_csv)
	ln_f1, ln_counts = extract_dictionaries(counts_csv)

	#t_f, t_sentiments = extract_dictionaries(twitter_sentiments_csv)
	#t_f1, t_counts = extract_dictionaries(twitter_counts_csv)

	features = ln_f
	for f in ln_f1 :
		features.add(f)
	#for f in t_f :
	#	features.add(f)
	#for f in t_f1 :
	#	features.add(f)

	specifications = get_phone_features()
	phones = specifications.keys()
	
	unwanted_phones = []

	all_features = read_all_features()
	
	for phone in specifications :
		phone_price = int(specifications[phone]['price'])
		if phone_price > exp_price + 50 or phone_price < exp_price - 50 :
			unwanted_phones.append(phone)
	
	
	for p in unwanted_phones :
		phones.remove(p)
	
	feature_phones = {}
	
	phone_names = {}
	for phone in phones :
		phone_names[phone] = specifications[phone]['phone']

	for feature in features_input :
		feature = all_features[feature]
		feature_phones[feature] = random.choice(phones)
	
	print feature_phones
	
	v = {}
	for feature in features_input :
		print feature
		feature1 = all_features[feature]
		phid = feature_phones[feature1]
		v[feature] = specifications[phid][feature]
	
	return v
