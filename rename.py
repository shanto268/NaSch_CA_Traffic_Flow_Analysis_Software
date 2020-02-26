#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:44:51 2020

@author: sshanto
"""

import os

# Lets change working directory to the pictures folder
os.chdir("/Users/sshanto/techmrt/Python_new/draft_2/experiment_1/figures")

def nto_(q3):
    q = []
    q4 = q3.split("_")
    for i in q4:
        if i == "dens":
            i = "density"
        q.append(i)
    res = "_".join(q)
    print(res)
    return res

for file in os.listdir("/Users/sshanto/techmrt/Python_new/draft_2/experiment_1/figures"):
     file_name, file_extension = os.path.splitext(file)
     if file_name[0] != "." :
         new_file_name = nto_(file_name)
         os.rename(file, new_file_name)    
     
