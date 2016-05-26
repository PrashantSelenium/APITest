'''
@This file is used to read from the excels, gather the info and do the appropriate parsing.
@Author : Runjhun Singh
'''
import openpyxl
import os, sys
currentFilePath = os.path.abspath(__file__)	
rootPath = "\\".join(currentFilePath.split("\\")[:-2])
sys.path.append(rootPath)
from openpyxl.styles import colors , Font, Color 
from utils.TestData import TestData
import ExecuteTestCase


filename = "\TestCase Repository.xlsx"
def get():
	input_file = getExcelFilePath(filename)
	readFromExcelSheet(input_file)	
	
def getExcelFilePath(filename):
	print "--finding path of the excel file----"
	currentFilePath = os.path.abspath(__file__)	
	rootPath = "\\".join(currentFilePath.split("\\")[:-2])
	input_file_path = rootPath+filename
	return input_file_path

def readFromExcelSheet(input_file_path):
	print "--- Reading from excel-----"
	wb = openpyxl.load_workbook(input_file_path)
	sheet = wb.get_sheet_by_name('TestSuite1')
	for row in range(2, sheet.max_row + 1):
		if (sheet['A' + str(row)].value != ""):
			testData = TestData(sheet,row)
			print testData.keyword
			responseJson = ExecuteTestCase.runAPI(testData)
			print responseJson
			# return testData

def writeIntoExcelSheet():
	a1 = sheet['K' + str(row)]
	ft = Font(color=colors.RED)
	a1.font = ft
	sheet['K' + str(row)] = str(json.dumps(responseJson))
	wb.save('Test Repo1.xlsx')



