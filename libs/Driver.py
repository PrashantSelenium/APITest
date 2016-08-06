#!/usr/bin/python

import sys, getopt
import os
import LoadEnvironment
import ReadWriteExcel
import ExecuteTestCase
import json
import requests
from jsoncompare import jsoncompare
import lxml.etree
from xml_diff import compare
from xml.etree.ElementTree import fromstring
from xml.etree import ElementTree as etree
import xml.etree.cElementTree as ET
import filecmp
from pprint import pprint
import xmltodict
from xml.etree.ElementTree import XML, fromstring, tostring


# def ordered(obj):
#     if isinstance(obj, dict):
#         return sorted((k, ordered(v)) for k, v in obj.items())
#     if isinstance(obj, list):
#         return sorted(ordered(x) for x in obj)
#     else:
#         return obj

# Compare respecting each array's order
def verifyResponse(expected_response,actual_response):
	try:
		jsoncompare.are_same(json.loads(expected_response),actual_response)
		print jsoncompare.are_same(json.loads(expected_response),actual_response)[0]
		print ("Compare Results:")	
		print ("###############################################")
		print jsoncompare.are_same(json.loads(expected_response),actual_response)
		print ("###############################################")
		print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
		return jsoncompare.are_same(json.loads(expected_response),actual_response)[0]
	except ValueError:
		print("data was not valid JSON")
		return False
	
# def dict_comp(d1, d2):
#     # compare dicts with identical structure
#     # return True if identical values,
#     # return False if a value is different
#     if d1 == d2:
#         return True
#     else:
#         for (k1, v1), (k2, v2) in zip(sorted(d1.items()), sorted(d2.items())):
#             if k1 == k2:
#                 if isinstance(v1, dict):
#                     return dict_comp(v1, v2)
#                 else:
#                     if v1 == v2:
#                         pass
#                     else:
#                         print("different values found at key --> "
#                               "{} <-- {} {} ".format(k1, v1, v2))
#                         return False

# Compare ignoring the value of certain keys
def verifyResponseIgnoring(expected_response,actual_response,parameter_to_ignore):
	try:		
		jsoncompare.are_same(json.loads(expected_response),actual_response,False, parameter_to_ignore)
		print (jsoncompare.are_same(json.loads(expected_response),actual_response,False, parameter_to_ignore)[0])
		print ("Compare Results:")
		print ("###############################################")
		print jsoncompare.are_same(json.loads(expected_response),actual_response,False, parameter_to_ignore)
		print ("###############################################")
		print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
		return jsoncompare.are_same(json.loads(expected_response),actual_response,False, parameter_to_ignore)[0]
	except ValueError:
		print("data was not valid JSON")
		return False

SHMART,username,password,AGENT,filename = LoadEnvironment.getEnvironment(sys.argv)
filename = "\\"+filename
workbook = ReadWriteExcel.openWorkbook(filename)
testcases,testsheet = ReadWriteExcel.getTotalTestCases(workbook)
print testcases

for testcase in range(2, testcases+1):
	testData = ReadWriteExcel.readFromExcelSheet(testcase,testsheet)
	print "In Driver -----" 
	# + testData.expected_response_body
	# print testData.method
	try:
		responseJson , response_code , api_type = ExecuteTestCase.runAPI(testData,SHMART,username,password,AGENT)
		print "In Driver after Execute "  + str(responseJson)
		print "In driver after execute response_code" + str(response_code)
	except requests.exceptions.HTTPError as e:
		responseJson =  "Error: " + str(e)
	# except Exception:
	# 	response_code = 500
	# 	# print "In driver after execute response_code" + str(response_code)
	# 	responseJson = "Unexpected Error with response code" + str(response_code) + "\n" + "Response :" + str(responseJson)
	# 	pass
	# print responseJson
	print api_type
	if api_type:
		print "in REST API Compare"
		teststatus = verifyResponseIgnoring(testData.expected_response_body,responseJson, testData.parameter_to_ignore)
	else :
		print "in SOAP API Compare"
		root = etree.fromstring(responseJson)
		x1 = etree.tostring(root)
		doc1 = xmltodict.parse(x1)
		root2 = etree.fromstring(testData.expected_response_body)
		x2 = etree.tostring(root2)
		doc2 = xmltodict.parse(x2)
		# print json.dumps(doc2)
		teststatus = verifyResponseIgnoring(json.dumps(doc1),json.loads(json.dumps(doc2)), testData.parameter_to_ignore)
		if (testData.parameter_to_write != ""):
			value_to_write = ReadWriteExcel.fetchValuesToWritefromResponse(doc1)
			# ReadWriteExcel.writeintoexcelTestData(filename,testData.parameter_to_write,value_to_write)
		# diff  = 0

		# if diff:
		# 	teststatus = 0
		# else:
		# 	teststatus = 1


	ReadWriteExcel.writeIntoExcelSheet(responseJson,testsheet,testcase,teststatus,api_type)
ReadWriteExcel.saveResults(workbook,filename)
