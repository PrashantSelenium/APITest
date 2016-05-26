'''
@This is used to process the APIs
@Author : Runjhun Singh
'''
import requests
from requests.auth import HTTPBasicAuth
import json
import os, sys
currentFilePath = os.path.abspath(__file__)	
rootPath = "\\".join(currentFilePath.split("\\")[:-2])
sys.path.append(rootPath)
import ReadWriteExcel 

base_url = "http://stag.shmart.in"
username = "0ada3354cbf5ef4c1848778cb415dbda"
password = "df2b09cbaf274a10833900e0dcc75f7f"

def runAPI(testData):

	if testData.method == "GET":
		test_url = base_url + testData.api_url_append
		response = requests.get(test_url, auth=HTTPBasicAuth(username, password))
	elif testData.method == "POST":
		test_url = base_url + testData.api_url_append
		headers = {'content-type': 'application/json'}
		response = requests.post(test_url, auth=HTTPBasicAuth(username, password),data=json.dumps(testData.request_body),headers=headers)
		responseJson = response.json()
	return responseJson