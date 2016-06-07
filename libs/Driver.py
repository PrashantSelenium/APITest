#!/usr/bin/python

import sys, getopt
import os
import LoadEnvironment
import ReadWriteExcel
import ExecuteTestCase
import json
from jsoncompare import jsoncompare


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

filename = "\TestCase Repository.xlsx"
SHMART,username,password = LoadEnvironment.getEnvironment(sys.argv)
workbook = ReadWriteExcel.openWorkbook(filename)
testcases,testsheet = ReadWriteExcel.getTotalTestCases(workbook)
for testcase in range(2, testcases+1):
	testData = ReadWriteExcel.readFromExcelSheet(testcase,testsheet)
	responseJson = ExecuteTestCase.runAPI(testData,SHMART,username,password)
	verifyResponseIgnoring(testData.expected_response_body,responseJson, testData.parameter_to_ignore)
	ReadWriteExcel.writeIntoExcelSheet(responseJson,testsheet,testcase)
ReadWriteExcel.saveResults(workbook,filename)