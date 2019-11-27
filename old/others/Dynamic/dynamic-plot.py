# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:40:49 2019

@author: Owner
"""
import matplotlib.pyplot as plt
import csv
import plotly.plotly as py
import plotly.graph_objs as go
from matplotlib import pylab
import seaborn as sns
from numpy import arange,array,ones
from scipy import stats
import numpy as np
from sklearn.linear_model import LinearRegression
#density , flow, updates, numlane, avgspeed
density5 = []
flow5 = []
updates5 = []
lan5 = []
avgspeed5 = []

with open('5.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density5.append(float(row[0]))
        flow5.append(float(row[1]))
        updates5.append(float(row[2]))
        lan5.append(float(row[3]))
        avgspeed5.append(float(row[4]))

density4 = []
flow4 = []
updates4 = []
lan4 = []
avgspeed4 = []

with open('4.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density4.append(float(row[0]))
        flow4.append(float(row[1]))
        updates4.append(float(row[2]))
        lan4.append(float(row[3]))
        avgspeed4.append(float(row[4]))
        
density45 = []
flow45 = []
updates45 = []
lan45 = []
avgspeed45 = []

with open('4.5.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density45.append(float(row[0]))
        flow45.append(float(row[1]))
        updates45.append(float(row[2]))
        lan45.append(float(row[3]))
        avgspeed45.append(float(row[4]))
        
density42= []
flow42= []
updates42= []
lan42= []
avgspeed42= []

with open('4.2.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density42.append(float(row[0]))
        flow42.append(float(row[1]))
        updates42.append(float(row[2]))
        lan42.append(float(row[3]))
        avgspeed42.append(float(row[4]))

density38= []
flow38  = []
updates38  = []
lan38  = []
avgspeed38  = []

with open('3.8.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density38.append(float(row[0]))
        flow38.append(float(row[1]))
        updates38.append(float(row[2]))
        lan38.append(float(row[3]))
        avgspeed38.append(float(row[4]))
        
density35= []
flow35  = []
updates35  = []
lan35  = []
avgspeed35  = []

with open('3.5.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density35.append(float(row[0]))
        flow35.append(float(row[1]))
        updates35.append(float(row[2]))
        lan35.append(float(row[3]))
        avgspeed35.append(float(row[4]))

density3= []
flow3  = []
updates3  = []
lan3  = []
avgspeed3  = []

with open('3.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density3.append(float(row[0]))
        flow3.append(float(row[1]))
        updates3.append(float(row[2]))
        lan3.append(float(row[3]))
        avgspeed3.append(float(row[4]))

density28= []
flow28  = []
updates28  = []
lan28  = []
avgspeed28  = []

with open('2.8.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density28.append(float(row[0]))
        flow28.append(float(row[1]))
        updates28.append(float(row[2]))
        lan28.append(float(row[3]))
        avgspeed28.append(float(row[4]))
        
density25= []
flow25  = []
updates25  = []
lan25  = []
avgspeed25  = []

with open('2.5.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density25.append(float(row[0]))
        flow25.append(float(row[1]))
        updates25.append(float(row[2]))
        lan25.append(float(row[3]))
        avgspeed25.append(float(row[4]))


density2= []
flow2  = []
updates2  = []
lan2  = []
avgspeed2  = []
lanerat2 = []
with open('2.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density2.append(float(row[0]))
        flow2.append(float(row[1]))
        updates2.append(float(row[2]))
        lan2.append(float(row[3]))
        avgspeed2.append(float(row[4]))




'''
plt.scatter(density5, flow5, color = 'g', s=1, marker = "o", label = 'Dynamic Lane Control: v < 5 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.show()
        

plt.figure(figsize=(30, 15))
plt.subplot(2,5,1)
plt.scatter(density5, flow5, color = 'g', s=1, marker = "o", label = 'Dynamic Lane Control: v < 5 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,5,2)
plt.scatter(density45, flow45, color = 'r', s=1, marker = "o", label = 'Dynamic Lane Control: v < 4.5 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,5,3)
plt.scatter(density42, flow42, color = 'r', s=1, marker = "o", label = 'Dynamic Lane Control: v < 4.2 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,5,4)
plt.scatter(density4, flow4, color = 'r', s=1, marker = "o", label = 'Dynamic Lane Control: v < 4 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,5,5)
plt.scatter(density38, flow38, color = 'b', s=1, marker = "o", label = 'Dynamic Lane Control: v < 3.8 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,5,6)
plt.scatter(density35, flow35, color = 'b', s=1, marker = "o", label = 'Dynamic Lane Control: v < 3.5 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,5,7)
plt.scatter(density3, flow3, color = 'b', s=1, marker = "o", label = 'Dynamic Lane Control: v < 3 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,5,8)
plt.scatter(density28, flow28, color = 'k', s=1, marker = "o", label = 'Dynamic Lane Control: v < 2.8 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,5,9)
plt.scatter(density25, flow25, color = 'k', s=1, marker = "o", label = 'Dynamic Lane Control: v < 2.5 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,5,10)
plt.scatter(density2, flow2, color = 'k', s=1, marker = "o", label = 'Dynamic Lane Control: v < 2 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig("dynamic-cases.pdf")
plt.show()
'''