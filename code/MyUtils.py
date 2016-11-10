import sys
import json
import requests

	
def sendpostdata(posturl, postdata, headers, result = None):
	try:
		result = requests.post(posturl, data = json.dumps(postdata), headers = headers)
		
		if str(result.status_code)[0] != '2' :
			return "Error status : " + str(result)
		
		return result.json()[0]
		
		return result
	except Exception as e:
		print e
		return "Error"
	return "Connect error. Check URL"
