#!/usr/bin/python

import sys, getopt
import os
import configparser
config_folder = "\config"

def getEnvironment(argumentList):
	"This fetches the environment used for execution"
	filename = sys.argv[2]

	for i in range(1,len(argumentList)):
		if argumentList[i].lower() == "prod":
			SHMART,username,password = getEnvData("prod")
			envFound = True
			break
		elif argumentList[i].lower() == "stag":
			SHMART,username,password = getEnvData("stag")
			envFound = True
			break
		elif argumentList[i].lower() == "qa":
			SHMART,username,password = getEnvData("qa")
			envFound = True
			break
		elif argumentList[i].lower() == "sandbox":
			SHMART,username,password = getEnvData("sandbox")
			envFound = True
			break
		envFound = False
	if (envFound == False):
		print "Please specify Environment like prod || stag || sandbox"
	return SHMART,username,password,filename

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