#!/usr/bin/python

import sys, getopt
import os
import LoadEnvironment
import ReadWriteExcel
import ExecuteTestCase
import json
from jsoncompare import jsoncompare


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj



# Compare respecting each array's order
def verifyResponse(expected_response,actual_response):
	try:
		ordered(json.loads(expected_response)) == ordered(actual_response)
		# json.loads(expected_response)
		# jsoncompare.are_same(json.loads(expected_response),actual_response)
	except ValueError:
		print("data was not valid JSON")
	print ("Compare Results:")	
	print jsoncompare.are_same(json.loads(expected_response),actual_response)
	print ("###############################################")
	print ("###############################################")
	print ("###############################################")



# Compare ignoring the value of certain keys
def verifyResponseIgnoring(expected_response,actual_response):
	jsoncompare.are_same(a, b, False, ["datetime", "snacktime"])
	print jsoncompare.are_same(json.loads(expected_response),actual_response)

filename = "\TestCase Repository.xlsx"
SHMART,username,password = LoadEnvironment.getEnvironment(sys.argv)
workbook = ReadWriteExcel.openWorkbook(filename)
testcases,testsheet = ReadWriteExcel.getTotalTestCases(workbook)
for testcase in range(2, testcases):
	testData = ReadWriteExcel.readFromExcelSheet(testcase,testsheet)
	# print testData.expected_response_body
	responseJson = ExecuteTestCase.runAPI(testData,SHMART,username,password)
	# print responseJson
	verifyResponse(testData.expected_response_body,responseJson)
	ReadWriteExcel.writeIntoExcelSheet(responseJson,testsheet,testcase)
ReadWriteExcel.saveResults(workbook,filename)