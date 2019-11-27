# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 02:11:50 2019

@author: Owner
"""
import matplotlib.pyplot as plt
import csv
from scipy import optimize
from scipy.optimize import curve_fit
import numpy as np

            

fn = 'cluster.txt'
fr = 'test-out.txt'
#dnewdata = "0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "
dnewdata = "dnew line"
with open(fn, 'r') as f:
    lines = f.read().split('\n')
    #to delete line use "del lines[4]"
    #to replace line:
    for i in range(0,len(lines)):    
        if (i % 100)  == 0 and i > 0:# or (i % 100) < 79 and i > 0:  #or (i % 4)  == 1 :
            lines[i] = dnewdata

with open(fr,'w') as f:
    f.write('\n'.join(lines))

with open(fr, "r") as f:
    lines = f.readlines()
with open(fr, "w") as f:
    for line in lines:
        if line.strip("\n") != "dnew line":
            f.write(line)
       
clnum = []
clusterhist = []
updates = []

with open(fr,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        clnum.append(float(row[0]))
        clusterhist.append(float(row[1]))
        updates.append(float(row[2]))
        

#print(clusternum)
plt.hist(clusterhist,bins=[4,5,6,7,8,9,10,11])
#plt.ylim(0,1800)
#plt.scatter(updates, clusternum)
plt.xlabel('Cluster Size')
plt.ylabel('Frequency')
plt.show()


plt.plot(updates, clnum)
plt.xlabel('time steps')
plt.ylabel('Total Number of Clusters')
plt.show()


