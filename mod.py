#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 13:51:04 2019

@author: ttumuon
"""
i = 0
x = []

while i != 3000:
    i+=1
    x.append(i)
    
for i in range(len(x)):    
    if (i % 100)  == 0 or (i % 100) < 19 and i > 0: 
        print(x[i])
