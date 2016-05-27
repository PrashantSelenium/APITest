import openpyxl

class TestCaseValues:
	"""Class to hold information read from each Excel Row """
	
	def __init__(self,sheet,row):	
		self.test = sheet['A'+str(row)].value
		self.test_case_no  = sheet['B' + str(row)].value
		self.api_name = sheet['B' + str(row)].value
		self.keyword    = sheet['C' + str(row)].value
		self.description = sheet['D' + str(row)].value
		self.method = sheet['E' + str(row)].value
		self.api_url_append =  sheet['F' + str(row)].value
		self.request_body   = sheet['G' + str(row)].value
		self.expected_response_body   = sheet['H' + str(row)].value
		self.expected_response_code  = sheet['I' + str(row)].value