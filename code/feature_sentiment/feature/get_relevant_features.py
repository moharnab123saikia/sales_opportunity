from nltk.corpus import wordnet

def read_feaures_csv() :
    import os

    DATAPATH = os.getcwd()
    DATAPATH = DATAPATH + os.sep + "relevant_features.csv"

    csv = open(DATAPATH, "r")
    features = {}
    for line in csv :
        content = line.split(",")
        features[content[0]] = content[1].split("\r")[0].split("\n")[0]
    return features

def read_phone_features(phone) :
    import os

    DATAPATH = os.getcwd()
    DATAPATH = DATAPATH + os.sep + "features_" + phone + ".txt"

    txt = open(DATAPATH)
    features = []
    for line in txt :
        features.append(line.split("\r")[0].split("\n")[0])
    return features

def find_similarity(feature_list1, feature_list2) :
    import itertools

    syns1 = {}
    for w in feature_list1 :
        w = w.strip()
        if len(w) > 0:
            try :
                syns1[w] = wordnet.synsets(w)
            except :
                pass


    syns2 = {}
    for w in feature_list2 :
        w = w.strip()
        if len(w) > 0 :
            try :
                syns2[w] = wordnet.synsets(w)
            except :
                pass

    words = list(itertools.product(feature_list1, feature_list2))

    similarity_scores = []
    for pair in words :
        try :
            s1 = syns1[pair[0]]
            s2 = syns2[pair[1]]

            if s1 and s2 :
                s =  s1[0].wup_similarity(s2[0])
                if s > 0.85:
                    similarity_scores.append((pair[0], pair[1], s))
        except :
            pass

    similarities = {}
    for val in similarity_scores :
        oldVal = similarities.get(val[0], (None, 0))
        if oldVal[1] == 0 :
            similarities[val[0]] = (val[1], val[2])
        else :
            if similarities[val[0]][1] < val[2] :
                similarities[val[0]] = (val[1], val[2])

    for val in similarities :
        similarities[val] = similarities[val][0]
    return similarities


phones = ['iphone_6', 'iphone_6plus', 'iphone_6s', 'iphone7', 'lg_g5', 'pixel', 'galaxy_s7']


features_static = read_feaures_csv().keys()

import os


s = []
for phone in phones :
    DATAPATH = os.getcwd()
    DATAPATH = DATAPATH + os.sep + "relevant_features_" + phone + ".csv"

    outputfile = open(DATAPATH, "w")

    phone_features = read_phone_features(phone)
    t = find_similarity(phone_features, features_static)
    for k, v in t.items() :
        outputfile.write(k + "," + v + "\n")
