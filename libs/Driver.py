#!/usr/bin/python

import sys, getopt
import os
import LoadEnvironment
import ReadWriteExcel


SHMART,username,password = LoadEnvironment.getEnvironment(sys.argv)
print SHMART
print username
print password