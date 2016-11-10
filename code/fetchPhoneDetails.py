import MyUtils


apiUrl = 'https://fonoapi.freshpixl.com/v1/'
apiKey = '82eb646d448f64b1513dd42561da18ad8845714113169823'

def getdevice( device, position=None, brand=None):
	url = apiUrl + 'getdevice'
	postdata = {'brand': brand,
				'device': device,
				'position': position,
				'token': apiKey
				}
	headers = {'content-type': 'application/json'}
	result = MyUtils.sendpostdata(url, postdata, headers)
	try:
		return result.json()
	except AttributeError:
		return result

if __name__ == '__main__':
	list_of_phones = [('apple', 'iphone 7'), ('apple', 'iphone 6s'), ('apple', 'iphone 6s plus'), ('apple', 'iphone 6 plus'), ('apple', 'iphone 6'), ('samsung', 'galaxy s7'), ('lg', 'g5'), ('google', 'pixel'), ('google', 'pixel xl')]
	featureSetMaster = set()
	features = {}
	for (b,p) in list_of_phones:
		f = getdevice(p, brand = b)
		features[b + p] = f
		[featureSetMaster.add(x) for x in f.keys()]
	
	outputfile = open('phonedetails.csv', 'w')
	outputfile.write('phone, ' + ', '.join(featureSetMaster) + '\r\n')
	for phone, values in features.items(): 
		s = phone
		for feature in featureSetMaster:
			if feature in values :
				k = values[feature]
				k = '%'.join(k.split('\r\n'))
				k = k.replace(',', ' ')
				k = k.replace(';', ' ')
				s = s + ', ' + k
			else :
				s = s + ', NULL'
		s = s.encode('utf-8')
		outputfile.write(s + "\r\n")

