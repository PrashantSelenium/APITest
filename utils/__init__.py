import os
import inspect

def setSystemPath():
	"""Sets sys.path to current directory so that modules can be imported easily""" 
	currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	parentdir = os.path.dirname(currentdir)
	os.sys.path.insert(0, parentdir)

setSystemPath()