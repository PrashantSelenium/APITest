'''
@This is used to process the APIs
@Author : Runjhun Singh
'''
import requests
from requests.auth import HTTPBasicAuth
import json
import os, sys
from bs4 import BeautifulSoup
# import xml.dom.minidom
# import tidylib
# currentFilePath = os.path.abspath(__file__)	
# rootPath = "\\".join(currentFilePath.split("\\")[:-2])
# sys.path.append(rootPath)
import ReadWriteExcel 

# base_url = "http://stag.shmart.in"
# username = "0ada3354cbf5ef4c1848778cb415dbda"
# password = "df2b09cbaf274a10833900e0dcc75f7f"

def runAPI(testData,SHMART,username,password,AGENT):
	print " in runAPI"
	base_url = SHMART 
	api_is_rest = 1

	if testData.method == "GET":
		# print "in Get------------------------------"
		test_url = base_url + testData.api_url_append + "/" +  testData.request_body
		# print test_url
		response = requests.get(test_url, auth=HTTPBasicAuth(username, password))
		responseJson = response.json()
		return responseJson , response , api_is_rest
	elif testData.method == "POST":
		# print "in post"
		test_url = base_url + testData.api_url_append
		print test_url
		print testData.request_body
		headers = {'content-type': 'application/json'}
		test_url = test_url.strip()
		response = requests.post(test_url, auth=HTTPBasicAuth(username, password),data=testData.request_body,headers=headers)
		print response
		responseJson = response.json()
		return responseJson , response , api_is_rest
	elif testData.method == "SOAP":
		print " in SOAP"
		base_url = AGENT
		api_is_rest = 0
		test_url = base_url + testData.api_url_append
		headers = {'content-type': 'application/soap+xml'}
		response = requests.post(test_url,data=testData.request_body,headers=headers)
		soapresponse = response.text
		print "In Execute ---" + soapresponse
		print response
		response = response.status_code 
		# xml = xml.dom.minidom.parse(soapresponse) # or xml.dom.minidom.parseString(xml_string)
		# pretty_xml_as_string = xml.toprettyxml()
		# print pretty_xml_as_string
		soapresponse = BeautifulSoup(soapresponse, "xml").prettify()
		# print response1
		# document, errors = tidy_document(soapresponse, options={'output_xml':1, 'indent':1, 'input_xml':1})
		# print document
		# rough_string = ElementTree.tostring(soapresponse, 'utf-8')
		# reparsed = minidom.parseString(rough_string)
		# print  reparsed.toprettyxml(indent="\t")

		return soapresponse , response , api_is_rest
