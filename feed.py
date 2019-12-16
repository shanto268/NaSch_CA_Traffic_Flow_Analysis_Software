#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# Read in the file
with open('/Users/ttumuon/muonSC8/sas/Python_new/config/case.py', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('lanes = 3', 'lanes = 5')
filedata = filedata.replace('length = 100', 'length = 200')

# Write the file out again
with open('/Users/ttumuon/muonSC8/sas/Python_new/config/case.py', 'w') as file:
  file.write(filedata)

#os.system("python inputs.py")

