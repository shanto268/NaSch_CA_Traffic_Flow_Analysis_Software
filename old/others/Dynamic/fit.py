# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 12:29:49 2019

@author: Owner
"""


import matplotlib.pyplot as plt
import csv
import plotly.plotly as py
import plotly.graph_objs as go
from matplotlib import pylab
from numpy import arange,array,ones
from scipy import stats
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

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


x35 = density35
y35 = flow35

x5 = density5
y5 = flow5

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])

p35 , e35 = optimize.curve_fit(piecewise_linear, x35, y35)
p5 , e5 = optimize.curve_fit(piecewise_linear, x5, y5)

xd = np.linspace(0, 1, 10000)
#plt.plot(x35, y35, "b.", x5, y5, "r.")
plt.plot(xd, piecewise_linear(xd, *p35), "b", xd, piecewise_linear(xd, *p5), "r")

