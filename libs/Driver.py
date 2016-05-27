#!/usr/bin/python

import sys, getopt
import os
import LoadEnvironment
import ReadWriteExcel
import ExecuteTestCase

filename = "\TestCase Repository.xlsx"
SHMART,username,password = LoadEnvironment.getEnvironment(sys.argv)
testcases,testsheet = ReadWriteExcel.getTotalTestCases(filename)
for testcase in range(2, testcases):
	testData = ReadWriteExcel.readFromExcelSheet(testcase,testsheet)
	responseJson = ExecuteTestCase.runAPI(testData,SHMART,username,password)
	print responseJson