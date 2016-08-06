import openpyxl
import requests
from requests.auth import HTTPBasicAuth
import json
from openpyxl.styles import colors
from openpyxl.styles import Font, Color

wb = openpyxl.load_workbook('Test Repo.xlsx')
sheet = wb.get_sheet_by_name('TestSuite1')
test_case_no  = sheet['A1'].value
print test_case_no
sheet['B1'].value = "Testing"
wb.save('Test Repo.xlsx')