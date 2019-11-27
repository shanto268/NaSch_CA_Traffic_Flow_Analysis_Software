from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import csv
import numpy, scipy, matplotlib
from scipy.optimize import curve_fit
from scipy.optimize import differential_evolution
import warnings

#density , flow, updates, numlane, avgspeed
density = []
flow = []
updates = []
lan = []
avgspeed = []

with open('dout.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density.append(float(row[0]))
        flow.append(float(row[1]))
        updates.append(float(row[2]))
        lan.append(float(row[3]))
        avgspeed.append(float(row[4]))

x = density
y = flow

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])

p0 = [np.mean(x), np.mean(y), 1, 1]

p , e = optimize.curve_fit(piecewise_linear, x, y, p0)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
xd = np.linspace(0, 1, 3000)
#plt.plot(x, y, "o")
plt.plot(xd, piecewise_linear(xd, *p), label = 'dedicated')
plt.legend()


'''
xData = numpy.array(density)
yData = numpy.array(flow)


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
    val = func(xData, *parameterTuple)
    return numpy.sum((yData - val) ** 2.0)


def generate_Initial_Parameters():
    # min and max used for bounds
    maxX = max(xData)
    minX = min(xData)
    maxY = max(yData)
    minY = min(yData)
    slope = 10000.0 * (maxY - minY) / (maxX - minX) # times 10 for safety margin

    parameterBounds = []
    parameterBounds.append([minX, maxX]) # search bounds for breakpoint
    parameterBounds.append([-slope, slope]) # search bounds for slopeA
    parameterBounds.append([minY, maxY]) # search bounds for offsetA
    parameterBounds.append([-slope, slope]) # search bounds for slopeB
    parameterBounds.append([minY, maxY]) # search bounds for offsetB


    result = differential_evolution(sumOfSquaredError, parameterBounds, seed=2)
    return result.x

# by default, differential_evolution completes by calling curve_fit() using parameter bounds
geneticParameters = generate_Initial_Parameters()

# call curve_fit without passing bounds from genetic algorithm
fittedParameters, pcov = curve_fit(func, xData, yData, geneticParameters)
#
print('Parameters:', fittedParameters)
print()

modelPredictions = func(xData, *fittedParameters) 

absError = modelPredictions - yData

SE = numpy.square(absError) # squared errors
MSE = numpy.mean(SE) # mean squared errors
RMSE = numpy.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (numpy.var(absError) / numpy.var(yData))

print()
print('RMSE:', RMSE)
print('R-squared:', Rsquared)

print()
#

##########################################################
# graphics output section
def ModelAndScatterPlot1(graphWidth, graphHeight):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    axes = f.add_subplot(111)

    # first the raw data as a scatter plot
    axes.scatter(xData, yData,  color = 'mediumblue', s=1, marker = "o")

    # create data for the fitted equation plot
    xModel = numpy.linspace(min(xData), max(xData))
    yModel = func(xModel, *fittedParameters)

    # now the model as a line plot
    axes.plot(xModel, yModel, 'orange')

    axes.set_xlabel('Density') # X axis data label
    axes.set_ylabel('Flow') # Y axis data label
    plt.title('Fundamental diagram: Dynamic: v < 2 and AV prop > 30%')
    plt.savefig("triangulate1.pdf")
    plt.show()
    plt.close('all') # clean up after using pyplot

def ModelAndScatterPlot2(graphWidth, graphHeight):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    axes = f.add_subplot(111)

    # first the raw data as a scatter plot

    # create data for the fitted equation plot
    xModel = numpy.linspace(min(xData), max(xData))
    yModel = func(xModel, *fittedParameters)

    # now the model as a line plot
    axes.plot(xModel, yModel)

    axes.set_xlabel('Density') # X axis data label
    axes.set_ylabel('Flow') # Y axis data label
    plt.title('Fundamental diagram: Dynamic: v < 2 and AV prop > 30%')
    plt.savefig("triangulate2.pdf")
    plt.show()
    plt.close('all')

graphWidth = 800
graphHeight = 600
ModelAndScatterPlot1(graphWidth, graphHeight)
ModelAndScatterPlot2(graphWidth, graphHeight)
'''