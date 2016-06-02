'''
@This file is used to read from the excels, gather the info and do the appropriate parsing.
@Author : Runjhun Singh
'''
import openpyxl
import openpyxl.cell
from openpyxl.utils import (_get_column_letter)

import os, sys
from openpyxl.styles import colors , Font, Color 
import ExecuteTestCase
import re
import json
import time
currentFilePath = os.path.abspath(__file__)	
rootPath = "\\".join(currentFilePath.split("\\")[:-2])
sys.path.append(rootPath)
from utils.TestCaseValues import TestCaseValues

def getRootPath():
	currentFilePath = os.path.abspath(__file__)	
	rootPath = "\\".join(currentFilePath.split("\\")[:-2])
	return rootPath

def getExcelFilePath(filename):
	# print "--finding path of the excel file----"
	# print rootPath
	rootPath = getRootPath()
	input_file_path = rootPath+filename
	return input_file_path

def openWorkbook(filename):
	global wb
	input_file_path = getExcelFilePath(filename)
	wb = openpyxl.load_workbook(input_file_path)
	return wb

def openExcelSheet(wb,sheet_name):
	print wb
	sheet = wb.get_sheet_by_name(sheet_name)
	return sheet

def getTotalTestCases(workbook):
	# input_file_path = getExcelFilePath(filename)
	sheet = openExcelSheet(workbook,"TestSuite1")
	row = sheet.max_row
	return row , sheet

def readFromExcelSheet(row,sheet):
	if (sheet['A' + str(row)].value != ""):
		testCaseValues = TestCaseValues(sheet,row)
		print testCaseValues.keyword
		# print testCaseValues.request_body
		testCaseValues.request_body = createRequestBody(testCaseValues.request_body)	
		# print testCaseValues.request_body
		return testCaseValues

def createRequestBody(request):
	# print request
	request = re.sub(r'#\w+', replaceData, request)
	return request

def replaceData(match):
	match = match.group()
	matching_value = getTestCaseValuesFromExcel(match)
	return  matching_value

def getTestCaseValuesFromExcel(variable):
	# print variable
	# input_file_path = getExcelFilePath("\TestCase Repository.xlsx")
	sheet = openExcelSheet(wb,"TestData")
	counter = 0
	for column in range(1,20):
	    column_letter = _get_column_letter(column)
	    for row in range(1,sheet.max_row):
	        if sheet[column_letter + str(row)].value == variable:
		        cell = sheet[column_letter + str(row+1)].value

		        return "\"" + str(cell) + "\""
		

def writeIntoExcelSheet(responseJson,sheet,row):
	a1 = sheet['K' + str(row)]
	ft = Font(color=colors.RED)
	a1.font = ft
	sheet['K' + str(row)] = str(json.dumps(responseJson))

def saveResults(workbook,filename):
	savelocation = getRootPath()
	print savelocation
	workbook.save( savelocation + '\TestExecution' + str(time.strftime("%Y%m%d-%H%M%S")) + '.xlsx')