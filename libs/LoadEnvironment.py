#!/usr/bin/python

import sys, getopt
import os
import configparser
config_folder = "\config"

# def getArgumentList(arg):
# 	"This gets number of command line arguments"
# 	argumentCount = len(arg)
# 	argumentList = []
# 	for i in range(0,argumentCount):
# 		argumentList.append(i) = sys.argv[i]
# 	 	# print argumentList
# 	# arguments = str(arg)
# 	# print arguments
# 	# argumentList = arguments.split(',')
# 	# print argumentList
# 	return argumentList

def getEnvironment(argumentList):
	"This fetches the environment used for execution"
	print sys.argv[0]
	testFile = sys.argv[2]

	for i in range(1,len(argumentList)):
		if argumentList[i].lower() == "prod":
			SHMART,username,password = getEnvData("prod")
			envFound = True
			break
		elif argumentList[i].lower() == "stag":
			SHMART,username,password = getEnvData("stag")
			envFound = True
			break
		elif argumentList[i].lower() == "sandbox":
			SHMART,username,password = getEnvData("sandbox")
			envFound = True
			break
		envFound = False
	if (envFound == False):
		print "Please specify Environment like prod || stag || sandbox"
	return SHMART,username,password,testFile

def getEnvData(api_env):

	currentFilePath = os.path.abspath(__file__)	
	rootPath = "\\".join(currentFilePath.split("\\")[:-2])
	configfile_path = rootPath+config_folder+"\\configuration.ini"
	config = configparser.ConfigParser()
	config.read(configfile_path)
	config.sections()
	if (api_env == "stag"):
		SHMART = config.get('STAGING', 'SHMART')
		username = config.get('STAGING', 'username')
		password = config.get('STAGING', 'password')
	elif (api_env == "prod"):
		SHMART = config.get('PRODUCTION', 'SHMART')
		username = config.get('PRODUCTION', 'username')
		password = config.get('PRODUCTION', 'password')
	elif (api_env == "sandbox"):
		SHMART = config.get('SANDBOX', 'SHMART')
		username = config.get('SANDBOX', 'username')
		password = config.get('SANDBOX', 'password')

	return SHMART,username,password

# if __name__ == "__main__":
#    	getEnvironment(sys.argv)