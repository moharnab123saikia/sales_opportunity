from bs4 import BeautifulSoup
import urllib2

DATAURLS = { "iphone7" :"http://www.phonearena.com/phones/Apple-iPhone-7_id9815", 'iphone_6' : 'http://www.phonearena.com/phones/Apple-iPhone-6_id8346', 'iphone_6plus' : 'http://www.phonearena.com/phones/Apple-iPhone-6-Plus_id8908', 'iphone_6s' : 'http://www.phonearena.com/phones/Apple-iPhone-6s_id9501', 'lg_g5' : 'http://www.phonearena.com/phones/LG-G5_id9819', 'pixel' : 'http://www.phonearena.com/phones/Google-Pixel_id10264', 'galaxy_s7' : 'http://www.phonearena.com/phones/Samsung-Galaxy-S7_id9817'}


def get_ratings(page_body) :
	spans = page_body.find_all("span", "s_rating_overal")
	res = {}
	res['phone_arena'] = spans[0].contents[0]
	if len(spans) > 2:
		res['phone_arena_overall'] = spans[1].contents[0]
	return res

def get_phone_specifications(page_body) :
	specifications_div = page_body.find_all(id = 'phone_specifications')
	feature_divs = page_body.find_all("li", "s_lv_1")
	features = {}
	
	for div in feature_divs :
		key = div.find_all("strong")[0].get_text().split(":")[0].strip()
		val = div.find_all("li")[0].get_text().strip()
		val = val.replace("\n", ";")
		val = val.replace(",", ";")
		features[key] = val

	return features

def get_variants(phone) :
	varis = []
	if phone == "iphone7" :
		v = {}
		v["Built-in storage"] = "32 GB"
		v["MSRP price"] = "$ 649"
		v['phone'] = phone
		varis.append(v)
		
		v = {}
		v["Built-in storage"] = "128 GB"
		v["MSRP price"] = "$ 749"
		v['phone'] = phone
		varis.append(v)
	if phone == "pixel":
		v = {}
		v["Built-in storage"] = "32 GB"
		v["MSRP price"] = "$ 649"
		v['phone'] = phone
		varis.append(v)
	if phone == "iphone_6":
		v = {}
		v["Built-in storage"] = "16 GB"
		v["MSRP price"] = "$ 649"
		v['phone'] = phone
		varis.append(v)
		
		v = {}
		v["Built-in storage"] = "64 GB"
		v["MSRP price"] = "$ 749"
		v['phone'] = phone
		varis.append(v)
	if phone == "iphone_6plus":
		v = {}
		v["Built-in storage"] = "16 GB"
		v["MSRP price"] = "$ 749"
		v['phone'] = phone
		varis.append(v)
		
		v = {}
		v["Built-in storage"] = "64 GB"
		v["MSRP price"] = "$ 849"
		v['phone'] = phone
		varis.append(v)
	if phone == "iphone_6s":
		v = {}
		v["Built-in storage"] = "16 GB"
		v["MSRP price"] = "$ 649"
		v['phone'] = phone
		varis.append(v)
		
		v = {}
		v["Built-in storage"] = "64 GB"
		v["MSRP price"] = "$ 749"
		v['phone'] = phone
		varis.append(v)
	if phone == "lg_g5":
		v = {}
		v['phone'] = phone
		varis.append(v)
	if phone == "galaxy_s7":
		v = {}
		v["Built-in storage"] = "32 GB"
		v["MSRP price"] = "$ 669"
		v['phone'] = phone
		varis.append(v)
	return varis

def form_all_dictionaries(f, v, r) :
	features = []
	for var in v:
		print var
		d = dict(f)
		d.update(var)
		d.update(r)
		features.append(d)
	return features

def get_details(phone, url) :
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page, "html.parser")
	page_body = soup.body

	ratings = get_ratings(page_body)
	features1 = get_phone_specifications(page_body)
	variants = get_variants(phone)
	features = form_all_dictionaries(features1, variants, ratings)
	
	return features

def table2csv(all_features) :
	import os
	
	DATAPATH = os.getcwd()
	DATAPATH = DATAPATH + os.sep + "phone_features.csv"
	
	features = set()
	for details in all_features :
		keys = details.keys()
		for f in keys :
			features.add(f)

	output_file = open(DATAPATH, "w")
	
	output_file.write("id")
	for f in features :
		output_file.write("," + f)
	output_file.write("\n")
	
	i = 1
	for details in all_features :
		output_file.write(str(i))
		i += 1
		for f in features :
			if f in details :
				output_file.write("," + details[f])
			else :
				output_file.write(",null")
		output_file.write("\n")

features = []
for phone, url in DATAURLS.items() :
	f = get_details(phone, url)
	for f1 in f :
		features.append(f1)
table2csv(features)
