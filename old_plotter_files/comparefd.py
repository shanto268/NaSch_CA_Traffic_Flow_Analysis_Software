# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:34:00 2019

@author: Owner
"""

from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import csv
import numpy, scipy, matplotlib
from scipy.optimize import curve_fit
from scipy.optimize import differential_evolution
import warnings

#density , flow, updates, numlane, avgspeed
densityn = []
flown = []
updatesn = []
lann = []
avgspeedn = []

densityd = []
flowd = []
updatesd = []
land = []
avgspeedd = []

densitydy = []
flowdy = []
updatesdy = []
landy = []
avgspeeddy = []

with open('nout.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        densityn.append(float(row[0]))
        flown.append(float(row[1]))
        updatesn.append(float(row[2]))
        lann.append(float(row[3]))
        avgspeedn.append(float(row[4]))

with open('dout.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        densityd.append(float(row[0]))
        flowd.append(float(row[1]))
        updatesd.append(float(row[2]))
        land.append(float(row[3]))
        avgspeedd.append(float(row[4]))
        
with open('dyout.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        densitydy.append(float(row[0]))
        flowdy.append(float(row[1]))
        updatesdy.append(float(row[2]))
        landy.append(float(row[3]))
        avgspeeddy.append(float(row[4]))
        


xDatan = numpy.array(densityn)
yDatan = numpy.array(flown)

xDatad = numpy.array(densityd)
yDatad = numpy.array(flowd)

xDatady = numpy.array(densitydy)
yDatady = numpy.array(flowdy)

def func(xArray, breakpoint, slopeA, offsetA, slopeB, offsetB):
    returnArray = []
    for x in xArray:
        if x < breakpoint:
            returnArray.append(slopeA * x + offsetA)
        else:
            returnArray.append(slopeB * x + offsetB)
    return returnArray


# function for genetic algorithm to minimize (sum of squared error)
def sumOfSquaredError(parameterTuple):
    warnings.filterwarnings("ignore") # do not print warnings by genetic algorithm
    val = func(xDatan, *parameterTuple)
    return numpy.sum((yDatan - val) ** 2.0)


def generate_Initial_Parametersdy():
    # min and max used for bounds
    maxX = max(xDatady)
    minX = min(xDatady)
    maxY = max(yDatady)
    minY = min(yDatady)
    slope = 10000.0 * (maxY - minY) / (maxX - minX) # times 10 for safety margin

    parameterBounds = []
    parameterBounds.append([minX, maxX]) # search bounds for breakpoint
    parameterBounds.append([-slope, slope]) # search bounds for slopeA
    parameterBounds.append([minY, maxY]) # search bounds for offsetA
    parameterBounds.append([-slope, slope]) # search bounds for slopeB
    parameterBounds.append([minY, maxY]) # search bounds for offsetB


    result = differential_evolution(sumOfSquaredError, parameterBounds, seed=2)
    return result.x


def generate_Initial_Parametersn():
    # min and max used for bounds
    maxX = max(xDatan)
    minX = min(xDatan)
    maxY = max(yDatan)
    minY = min(yDatan)
    slope = 10000.0 * (maxY - minY) / (maxX - minX) # times 10 for safety margin

    parameterBounds = []
    parameterBounds.append([minX, maxX]) # search bounds for breakpoint
    parameterBounds.append([-slope, slope]) # search bounds for slopeA
    parameterBounds.append([minY, maxY]) # search bounds for offsetA
    parameterBounds.append([-slope, slope]) # search bounds for slopeB
    parameterBounds.append([minY, maxY]) # search bounds for offsetB


    result = differential_evolution(sumOfSquaredError, parameterBounds, seed=10)
    return result.x


def generate_Initial_Parametersd():
    # min and max used for bounds
    maxX = max(xDatad)
    minX = min(xDatad)
    maxY = max(yDatad)
    minY = min(yDatad)
    slope = 10000.0 * (maxY - minY) / (maxX - minX) # times 10 for safety margin

    parameterBounds = []
    parameterBounds.append([minX, maxX]) # search bounds for breakpoint
    parameterBounds.append([-slope, slope]) # search bounds for slopeA
    parameterBounds.append([minY, maxY]) # search bounds for offsetA
    parameterBounds.append([-slope, slope]) # search bounds for slopeB
    parameterBounds.append([minY, maxY]) # search bounds for offsetB


    result = differential_evolution(sumOfSquaredError, parameterBounds, seed=4)
    return result.x


# by default, differential_evolution completes by calling curve_fit() using parameter bounds
geneticParametersn = generate_Initial_Parametersn()
geneticParametersd = generate_Initial_Parametersd()
geneticParametersdy = generate_Initial_Parametersdy()


# call curve_fit without passing bounds from genetic algorithm
fittedParametersn, pcovn = curve_fit(func, xDatan, yDatan, geneticParametersn)
fittedParametersd, pcovd = curve_fit(func, xDatad, yDatad, geneticParametersd)
fittedParametersdy, pcovdy = curve_fit(func, xDatady, yDatady, geneticParametersdy)





'''
print('Parameters:', fittedParameters)
print()

modelPredictions = func(xDatan, *fittedParameters) 

absError = modelPredictions - yDatan

SE = numpy.square(absError) # squared errors
MSE = numpy.mean(SE) # mean squared errors
RMSE = numpy.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (numpy.var(absError) / numpy.var(yDatan))

print()
print('RMSE:', RMSE)
print('R-squared:', Rsquared)

print()
'''

##########################################################
# graphics output section
graphWidth = 800
graphHeight = 600


    # first the raw Datan as a scatter plot

    # create Datan for the fitted equation plot
xModeln = numpy.linspace(min(xDatan), max(xDatan))
yModeln = func(xModeln, *fittedParametersn)


xModeld = numpy.linspace(min(xDatad), max(xDatad))
yModeld = func(xModeld, *fittedParametersd)

xModeldy = numpy.linspace(min(xDatady), max(xDatady))
yModeldy = func(xModeldy, *fittedParametersdy)
    # now the model as a line plot
plt.plot(xModeln, yModeln, 'r', label = 'No Control')
plt.plot(xModeld, yModeld, 'orange', label = 'Dedicated')
plt.plot(xModeldy, yModeldy, 'b', label = 'Dynamic: v < 2 and AV > 30%')
plt.xlabel('Density') # X axis Datan label
plt.ylabel('Flow') # Y axis Datan label
plt.legend()
plt.title('Fundamental diagram')
plt.savefig("fdfinal.pdf")
plt.show()
plt.close('all')


