'''
@This file is used to read from the excels, gather the info and do the appropriate parsing.
@Author : Runjhun Singh
'''
import openpyxl
import os, sys
from openpyxl.styles import colors , Font, Color 
import ExecuteTestCase
currentFilePath = os.path.abspath(__file__)	
rootPath = "\\".join(currentFilePath.split("\\")[:-2])
sys.path.append(rootPath)
from utils.TestData import TestData

# def startProcess(SHMART,username,password):
# input_file = getExcelFilePath(filename)
# 	readFromExcelSheet(filename,SHMART,username,password)	
sheet_name = "TestSuite1"
	
def getExcelFilePath(filename):
	print "--finding path of the excel file----"
	currentFilePath = os.path.abspath(__file__)	
	rootPath = "\\".join(currentFilePath.split("\\")[:-2])
	print rootPath
	input_file_path = rootPath+filename
	return input_file_path

def getTotalTestCases(filename):
	input_file_path = getExcelFilePath(filename)
	wb = openpyxl.load_workbook(input_file_path)
	sheet = wb.get_sheet_by_name(sheet_name)
	row = sheet.max_row
	return row , sheet

def readFromExcelSheet(row,sheet):
	# input_file_path = getExcelFilePath(filename)
	# wb = openpyxl.load_workbook(input_file_path)
	# sheet = wb.get_sheet_by_name(sheet_name)
	# for row in range(2, sheet.max_row + 1):
	if (sheet['A' + str(row)].value != ""):
		testData = TestData(sheet,row)
		print testData.keyword
		return testData

def writeIntoExcelSheet():
	a1 = sheet['K' + str(row)]
	ft = Font(color=colors.RED)
	a1.font = ft
	sheet['K' + str(row)] = str(json.dumps(responseJson))
	wb.save('Test Repo1.xlsx')



