#!/usr/bin/python

import sys, getopt
import os
import LoadEnvironment
import ReadWriteExcel
import ExecuteTestCase
import json
from jsoncompare import jsoncompare


# Compare respecting each array's order
def verifyResponse(expected_response,actual_response):
	jsoncompare.are_same(json.loads(expected_response),actual_response)
	print jsoncompare.are_same(json.loads(expected_response),actual_response)

# Compare ignoring the value of certain keys
def verifyResponseIgnoring(expected_response,actual_response):
	jsoncompare.are_same(a, b, False, ["datetime", "snacktime"])
	print jsoncompare.are_same(json.loads(expected_response),actual_response)

filename = "\TestCase Repository Test.xlsx"
SHMART,username,password = LoadEnvironment.getEnvironment(sys.argv)
# print username
workbook = ReadWriteExcel.openWorkbook(filename)
testcases,testsheet = ReadWriteExcel.getTotalTestCases(workbook)
print testcases
for testcase in range(2, testcases+1):
	testData = ReadWriteExcel.readFromExcelSheet(testcase,testsheet)
	print testData.expected_response_body
	# print testData.method
	responseJson = ExecuteTestCase.runAPI(testData,SHMART,username,password)
	print responseJson
	verifyResponse(testData.expected_response_body,responseJson)
	ReadWriteExcel.writeIntoExcelSheet(responseJson,testsheet,testcase)
ReadWriteExcel.saveResults(workbook,filename)