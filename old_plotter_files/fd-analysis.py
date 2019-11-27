# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:42:46 2019

@author: Owner
"""

import pylab
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import csv
from scipy import optimize
from scipy.optimize import curve_fit
import numpy as np
from astropy import modeling
from PyPDF2 import PdfFileMerger
avpercent = 50                                                          #  ''' change this!!!!'''

            
            #input file: raw data: case_letter + info.txt e.g. dinfo.txt for dedicated case  
            #output file: dout1.txt
                        #process 1: raw data --> process data file
fn = 'r1m1a.txt'
fr = 'fdnout1.txt'
#dnewdata = "0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "
dnewdata = "dnew line"
with open(fn, 'r') as f:
    lines = f.read().split('\n')
    #to delete line use "del lines[4]"
    #to replace line:
    for i in range(0,len(lines)):    
        if (i % 100)  == 0 or (i % 100) < 19 and i > 0:  #or (i % 4)  == 1 :
            lines[i] = dnewdata
with open(fr,'w') as f:
    f.write('\n'.join(lines))

with open(fr, "r") as f:
    lines = f.readlines()
with open(fr, "w") as f:
    for line in lines:
        if line.strip("\n") != "dnew line":
            f.write(line)
            
with open(fr, "r+") as f:     #fr change
    a = f.read()

with open(fr, "w+") as f:     #fr change
        f.write("0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  \n" + a)
            
                                # plotting data ready  
                    
density = []
flow = []
updates = []
lan = []
avgspeed = []
trigbin = []
cspeed = []
count1 = 0
count2 = 0
avprop = []
newflow = []
densityrv = []
flowrv = []
densityav = []
flowav = []        


with open(fr,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density.append(float(row[0]))
        flow.append(float(row[1]))
        updates.append(float(row[2]))
        densityrv.append(float(row[3]))
        flowrv.append(float(row[4]))
        densityav.append(float(row[5]))
        flowav.append(float(row[6]))

                                        # data arranged as below:        
#density, flow, updates, densityrv, flowrv, densityav, flowav
                                
str3 = "No Control: AV ~ " + str(avpercent)+ "%"

#print("Overall flow:" + str(max(flow)))
flow_max_index = flow.index(max(flow))
#print("density at max flow: " +str(density[flow_max_index]))
#print("RV flow:" + str(max(flowrv)))
flowrv_max_index = flowrv.index(max(flowrv))
#print("density at max flowrv: " +str(densityrv[flowrv_max_index]))
#print("AV flow:" + str(max(flowav)))
flowav_max_index = flowav.index(max(flowav))
#print("density at max flow: " +str(densityav[flowav_max_index]))

x = density
y =flow
N= 3000

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])

p0 = [np.mean(x), np.mean(y), 1, 1]
            #weighing functions:            
            
y_weight = np.empty(len(y))
y_weight.fill(10)
y_weight[0] = y_weight[-5:-1] = 0.1
y_weight[flow_max_index] = 0.2


p , e = optimize.curve_fit(piecewise_linear, x, y, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
xd = np.linspace(0, 1, N)

x0, y0, k1, k2 = p
                                                                        #function and coefficients
y_crit = y0 #max flow
x_crit = x0 #critical density
x_jam = max(xd) #jam density
def x_intercept(slope, yi, xi):
    return (slope*xi - yi)/ slope
x_jam = min(x_intercept(k2, y0, x0),1)
free_y = k1   #slope 1
wave_v = k2    #slope 2

#textstr = r'$q_{free flow} = %3f , \rho_{critical} = %3f , q_{max} = %3f , w = %3f$' % (k1,x0, y0, k2)
#plt.plot(x, y, "o")
plt.plot(xd, piecewise_linear(xd, *p), 'orange', label = 'fit')
plt.scatter(x,y,color = 'mediumblue', s=3, marker = ".", label = 'data')
plt.legend()
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental diagram: ' + str3)
#plt.text(1.2, 0.5, textstr, fontsize=12)
#plt.subplots_adjust(left=0.25)
#plt.savefig(fig10)
plt.show()


print("[x_critical  y_max  free_flow_v  wave_speed]")
print(p)
print("jam density: " + str(x_jam))
                                                #RV FD FIT
xrv = densityrv
yrv= flowrv

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])

p0 = [np.mean(xrv), np.mean(yrv), 1, 1]

#weighing functions:            
            
y_weight = np.empty(len(yrv))
y_weight.fill(10)
y_weight[0] = y_weight[-5:-1] = 0.1
y_weight[flowrv_max_index] = 0.2


prv , e = optimize.curve_fit(piecewise_linear, xrv, yrv, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
#xdrv = np.linspace(0, max(xrv), 3000)
xdrv = np.linspace(0, 1, 3000)


x0, y0, k1, k2 = prv
                                                                        #function and coefficients
y_crit = y0 #max flow
x_crit = x0 #critical density
y_array = np.array(piecewise_linear(xdrv, *prv))
free_y = k1   #slope 1
wave_v = k2    #slope 2

def x_intercept(slope, yi, xi):
    return (slope*xi - yi)/ slope
x_jam = x_intercept(k2, y0, x0)

#plt.plot(x, y, "o")
plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'orange', label = 'fit')
plt.scatter(xrv,yrv,color = 'mediumblue', s=3, marker = ".", label = 'data')
plt.legend()
plt.xlabel('density')
plt.ylabel('flow')
plt.gca().set_xlim([0,max(densityrv)+0.05])
plt.gca().set_ylim([0, max(flowrv) + 0.05])
plt.title('RV Fundamental diagram: ' + str3)
#plt.savefig(fig13)
plt.show()


print("[x_critical  y_max  free_flow_v  wave_speed]")
print(prv)
print("jam density: " + str(x_jam))
                                                #AV FD FIT
xav = densityav
yav= flowav

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])

p0 = [np.mean(xav), np.mean(yav), 1, 1]

#weighing functions:            
            
y_weight = np.empty(len(yav))
y_weight.fill(10)
#print(len(y_weight))
#y_weight[0] = 0.1
y_weight[0] = y_weight[-5:-1] = 0.1
y_weight[flowav_max_index] = 0.2

pav , e = optimize.curve_fit(piecewise_linear, xav, yav, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
xdav = np.linspace(0, max(xav)+0.05, 3000)
#plt.plot(x, y, "o")

x0, y0, k1, k2 = pav
                                                                        #function and coefficients
y_crit = y0 #max flow
x_crit = x0 #critical density
def x_intercept(slope, yi, xi):
    return (slope*xi - yi)/ slope
x_jam = x_intercept(k2, y0, x0)
free_y = k1   #slope 1
wave_v = k2    #slope 2



plt.plot(xdav, piecewise_linear(xdav, *pav), 'orange', label = 'fit')
plt.scatter(xav,yav,color = 'mediumblue', s=3, marker = ".", label = 'data')
plt.legend()
plt.xlabel('density')
plt.ylabel('flow')
plt.title('AV Fundamental diagram: ' + str3)
plt.gca().set_xlim([0,max(densityav)+0.05])
plt.gca().set_ylim([0, max(flowav) + 0.05])
#plt.savefig(fig14)
plt.show()
print("[x_critical  y_max  free_flow_v  wave_speed]")
print(pav)
print("jam density: " + str(x_jam))

                                                                       #FD AV RV
plt.plot(xdav, piecewise_linear(xdav, *pav), 'red', label = 'AV')
plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'blue', label = 'RV')
plt.gca().set_xlim([0,1])
plt.gca().set_ylim([0, max((max(flowrv) + 0.05),(max(flowav) + 0.05)) ])
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental diagram: ' + str3)
plt.legend()
#plt.savefig(fig16)
plt.show()

                                                    #FD ALL

plt.plot(xdav, piecewise_linear(xdav, *pav), 'red', label = 'AV')
plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'blue', label = 'RV')
plt.plot(xd, piecewise_linear(xd, *p), 'orange', label = 'Overall')
plt.xlabel('density')
plt.ylabel('flow')
plt.gca().set_xlim([0,1])
plt.gca().set_ylim([0, max(flow) +0.05])
plt.title('Fundamental diagram: ' + str3)
plt.legend()
#plt.savefig(fig23)
plt.show()

