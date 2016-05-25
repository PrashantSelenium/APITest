import openpyxl
import requests
from requests.auth import HTTPBasicAuth
import json
from openpyxl.styles import colors
from openpyxl.styles import Font, Color

wb = openpyxl.load_workbook('Test Repo.xlsx')
sheet = wb.get_sheet_by_name('TestSuite1')
base_url = "http://stag.shmart.in"
username = "0ada3354cbf5ef4c1848778cb415dbda"
password = "df2b09cbaf274a10833900e0dcc75f7f"
for row in range(2, sheet.max_row + 1):
	if (sheet['A' + str(row)].value != ""):
		test_case_no  = sheet['A' + str(row)].value
       	api_name = sheet['B' + str(row)].value
       	keyword    = sheet['C' + str(row)].value
       	request_body   = sheet['G' + str(row)].value
       	api_url_append =  sheet['F' + str(row)].value
       	method = sheet['E' + str(row)].value
       	print test_case_no , request_body , 

	if method == "GET":
		test_url = base_url + api_url_append
 		response = requests.get(test_url, auth=HTTPBasicAuth(username, password))
	elif method == "POST":
		test_url = base_url + api_url_append
		headers = {'content-type': 'application/json'}
		response = requests.post(test_url, auth=HTTPBasicAuth(username, password),data=json.dumps(request_body),headers=headers)
		responseJson = response.json()
		print responseJson
	a1 = sheet['K' + str(row)]
	ft = Font(color=colors.RED)
	a1.font = ft
	sheet['K' + str(row)] = str(json.dumps(responseJson))

wb.save('Test Repo1.xlsx')