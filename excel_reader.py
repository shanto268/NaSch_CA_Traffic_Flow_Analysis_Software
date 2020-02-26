#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:56:04 2020

@author: sshanto
"""
from pandas import read_excel
# find your sheet name at the bottom left of your excel file and assign 
# it to my_sheet 
my_sheet = 'Sheet1'
file_name = 'exp_param.xlsx' # name of your excel file
df = read_excel(file_name, sheet_name = my_sheet)
print(df.info())