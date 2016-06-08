'''
@This is used to process the APIs
@Author : Runjhun Singh
'''
import requests
from requests.auth import HTTPBasicAuth
import json
import os, sys
# currentFilePath = os.path.abspath(__file__)	
# rootPath = "\\".join(currentFilePath.split("\\")[:-2])
# sys.path.append(rootPath)
import ReadWriteExcel 

# base_url = "http://stag.shmart.in"
# username = "0ada3354cbf5ef4c1848778cb415dbda"
# password = "df2b09cbaf274a10833900e0dcc75f7f"

def runAPI(testData,SHMART,username,password):
	base_url = SHMART 
	if testData.method == "GET":
<<<<<<< HEAD
		test_url = base_url + testData.api_url_append + "/" + testData.request_body
=======
		print "in Get------------------------------"
		test_url = base_url + testData.api_url_append + "/" +  testData.request_body
		print test_url
>>>>>>> 768a537bfab8830ac401f7be83821eac4d50bb1f
		response = requests.get(test_url, auth=HTTPBasicAuth(username, password))
		responseJson = response.json()
	elif testData.method == "POST":
		print "in post"
		test_url = base_url + testData.api_url_append
		print test_url
		print testData.request_body
		headers = {'content-type': 'application/json'}
		test_url = test_url.strip()
		response = requests.post(test_url, auth=HTTPBasicAuth(username, password),data=testData.request_body,headers=headers)
		print response
		responseJson = response.json()
	return responseJson