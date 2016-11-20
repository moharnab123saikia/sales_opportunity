import json

def read_all_features() :
    import os
    DATAPATH = os.getcwd()
    DATAPATH = os.sep.join(DATAPATH.split(os.sep)[ : -1])
    DATAPATH = DATAPATH + os.sep + "output" + os.sep + "sentiment_scores" + os.sep + "all_features.csv"

    features = {}
    _file = open(DATAPATH, "r")
    for line in _file :
        content = line.split(",")
        features[content[0]] = content[1].split("\r")[0].split("\n")[0]
    return features

def read_feature_file(filename, master_features) :
    _file = open(filename, "r")

    content = _file.read()
    data = json.loads(content)['data']

    feature_s = {}
    feature_c = {}
    for phonedata in data :
        phone = phonedata.keys()[0]
        pfeatures = phonedata[phone]
        phone_feature_count = {}
        phone_feature_sentiment = {}
        for k, v in pfeatures.items() :
            klass = master_features[k]
            if klass in phone_feature_count :
                oldCount = phone_feature_count[klass]
                oldSenti = phone_feature_sentiment[klass]

                newCount = oldCount + int(v[0])
                newSenti = ( float(oldCount * oldSenti) + float(v[0] * v[1]) ) / newCount

                phone_feature_count[klass] = newCount
                phone_feature_sentiment[klass] = newSenti
            else :
                phone_feature_count[klass] = int(v[0])
                phone_feature_sentiment[klass] = float(v[1])


        feature_s[phone] = phone_feature_sentiment
        feature_c[phone] = phone_feature_count
    return (feature_c, feature_s)

def read_tweet_features(master_features) :
    import os
    DATAPATH = os.getcwd()
    DATAPATH = os.sep.join(DATAPATH.split(os.sep)[ : -1])
    DATAPATH = DATAPATH + os.sep + "output" + os.sep + "sentiment_scores" + os.sep + "twitter_data.txt"
    return read_feature_file(DATAPATH, master_features)


def table2csv(features, titles) :
    feature_c = features[0]
    feature_s = features[1]

    import os
    DATAPATH = os.getcwd()
    DATAPATH += os.sep
    cfile = open(DATAPATH + "twitter_counts.csv", "w")
    sfile = open(DATAPATH + "twitter_sentiments.csv", "w")

    cfile.write("phones")
    for title in titles :
        cfile.write("," + titles[title])
    cfile.write("\n")

    sfile.write("phones")
    for title in titles :
        sfile.write("," + titles[title])
    sfile.write("\n")

    for phone in feature_c :
        cfile.write(phone)
        counts = feature_c[phone]
        for feature in titles :
            feature = titles[feature]
            cfile.write(",%d" % counts.get(feature, 0))
        cfile.write("\n")

        sfile.write(phone)
        sentiments = feature_s[phone]
        for feature in titles :
            feature = titles[feature]
            sfile.write(",%f" % sentiments.get(feature, 0.0))
        sfile.write("\n")

master_features = read_all_features()
#print sorted(master_features.values())
features = read_tweet_features(master_features)
#print dynamic_features[1]
table2csv(features, master_features)
