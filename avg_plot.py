#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 12:25:25 2020

@author: sshanto
"""
import random 
import numpy as np
import matplotlib.pyplot as plt


    
    
x = [i for i in range(120)]
y = [random.randint(-5,4)*np.sin(x[i]/random.randint(100,121)) for i in range(len(x))]
plt.plot(x,y)
plt.show()

print(y)

yi = []
for i in range(len(x)-1):
   yi.append((y[i+1]+y[i])/2)

print(yi)


xi = [i for i in range(len(yi))]

plt.plot(xi,yi)
plt.show()