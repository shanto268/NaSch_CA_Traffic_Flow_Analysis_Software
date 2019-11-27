# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:00:22 2019

@author: Owner
"""

import pylab
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
import csv
from scipy import optimize
from scipy.optimize import curve_fit
import numpy as np
from astropy import modeling
from PyPDF2 import PdfFileMerger
     
       
            #input file: raw data: case_letter + info.txt e.g. dinfo.txt for dedicated case  
            #output file: dout1.txt
                        #process 1: raw data --> process data file
fn = 'dinfo50.txt'
fr = 'dout50.txt'
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
            
with open(r"dout50.txt", "r+") as f:     #fr change
    a = f.read()

with open(r"dout50.txt", "w+") as f:     #fr change
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
        
with open('nout50.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        density.append(float(row[0]))
        flow.append(float(row[1]))
        updates.append(float(row[2]))
        lan.append(float(row[3]))
        avgspeed.append(float(row[4]))
        trigbin.append(float(row[5]))        
        cspeed.append(float(row[6]))
        avprop.append(float(row[7]))
        newflow.append(float(row[8]))
        densityrv.append(float(row[9]))
        flowrv.append(float(row[10]))
        densityav.append(float(row[11]))
        flowav.append(float(row[12]))

                                        # data arranged as below:        
# density, flow, updates, number of lane changes, avg speed, trig status, control speed, prop of av, new flow, density of rv, flow of rv, density of av, flow of av, 

                                            # lane change rate
lrat = []
lratev = []
lratodd = []
lanerate = []
avpropcons = []
conspeed = []

for lane in lan:
    count1 += 1
    if (count1 % 100) == 0:
        lrat.append(lan[count1])

for i in range(len(lrat)):
    if (i%2) == 0:
        lratev.append(lrat[i])        
    else:
        lratodd.append(lrat[i])        

for j in range(min(len(lratev),len(lratodd))):
    lanerate.append(lratodd[j]-lratev[j])

tp = np.arange(len(lanerate))
lr = np.array(lanerate)

avthresh = 30
vthresh = 3                                   #control v

for element in range(len(updates)):
    avpropcons.append(avthresh)                    
    conspeed.append(vthresh)                                              
    
#print(updates)    

                                #fig names
fig1 = "v6/n/trigcondv.pdf"    
fig2 = "v6/n/trigcondav.pdf"
fig3 = "v6/n/lcrate.pdf"
fig4 = "v6/n/numlane.pdf"
fig5 = "v6/n/trigstatus.pdf"
fig6 = "v6/n/fddata.pdf"
fig7 = "v6/n/newflowfd.pdf"
fig8 = "v6/n/fd-rv.pdf"
fig9 = "v6/n/fd-av.pdf"
fig10 = "v6/n/fdfit.pdf"
fig11 = "v6/n/rhov.pdf"
fig12 = "v6/n/summary/result-nc.pdf"
fig13 = "v6/n/fdfitrv.pdf"
fig14 = "v6/n/fdfitav.pdf"
fig15 = "v6/n/drvdav.pdf"
fig16 = "v6/n/fdrvav.pdf"                       
                                     #graph labels

str1 = "Dynamic: v < " + str(vthresh) + " AV > " + str(avthresh)
str2 = "Dedicated " 
str3 = "No Control"
                                #flow analysis:

fig = plt.figure()
ax = plt.axes(projection="3d")

z_line = np.array(flow)
x_line = np.array(flowrv)
y_line = np.array(flowav)
#ax.plot3D(x_line, y_line, z_line, 'gray')

z_points = flow
x_points = flowrv
y_points = flowav
ax.scatter3D(x_points, y_points, z_points, c=z_points, s= 3);
ax.set_xlabel('flow RV')
ax.set_ylabel('flow AV')
ax.set_zlabel('Overall flow')
#plt.zlabel("Overall flow")
plt.show()

# Example points that use a color proportional to the radial distance

X = x_line
Y = y_line
Z = z_line

pylab.scatter(X,Y,c=Z,linewidths=.01)
pylab.axis('equal')
pylab.show()

x = x_line
y = y_line
z = z_line

fig = plt.figure()
ax = Axes3D(fig)
surf = ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.1)
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('flow RV')
ax.set_ylabel('flow AV')
ax.set_zlabel('Overall flow')
#plt.savefig()
plt.show()

