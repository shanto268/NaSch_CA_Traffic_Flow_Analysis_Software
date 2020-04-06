#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:34:31 2020

@author: sshanto
"""

import glob
import matplotlib.pyplot as plt
import pandas as pd

def createPlot(file, index, label, title):
    data = pd.read_csv(file, index_col = index)
    plt.plot(data)
    plt.ylabel(label)
    plt.title(title)
    
fileNames = glob.glob("*.txt")
for file in fileNames:
   # createPlot(file,0,"Density","System Density")
    createPlot(file,13,"Flow","System Flow")
### Generate the plot
plt.show()
