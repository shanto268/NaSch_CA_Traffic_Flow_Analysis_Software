# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:32:43 2019

@author: Owner
"""

import matplotlib.pyplot as plt
import csv

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

densityn = []
flown = []
updatesn = []
lann = []
avgspeedn = []

with open('dyout.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        densitydy.append(float(row[0]))
        flowdy.append(float(row[1]))
        updatesdy.append(float(row[2]))
        landy.append(float(row[3]))
        avgspeeddy.append(float(row[4]))

with open('dout.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        densityd.append(float(row[0]))
        flowd.append(float(row[1]))
        updatesd.append(float(row[2]))
        land.append(float(row[3]))
        avgspeedd.append(float(row[4]))
        
with open('nout.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        densityn.append(float(row[0]))
        flown.append(float(row[1]))
        updatesn.append(float(row[2]))
        lann.append(float(row[3]))
        avgspeedn.append(float(row[4]))
        
plt.figure(figsize=(10, 10))
plt.subplot(2,1,1)
plt.plot(densityn, flown, 'b', label = 'No control') # plotting t, a separately 
plt.plot(densityd, flowd, 'r', label = 'Dedicated Lane Control') # plotting t, b separately 
plt.plot(densitydy, flowdy, 'g', label = 'Dynamic Lane Control: v < 4.2 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,1,2)
plt.scatter(densityn, flown, color = 'b', s=6, marker = "v", label = 'No control') # plotting t, a separately 
plt.scatter(densityd, flowd, color = 'r', s=6, marker = ">", label = 'Dedicated Lane Control') # plotting t, b separately 
plt.scatter(densitydy, flowdy, color = 'g', s=6, marker = "<", label = 'Dynamic Lane Control: v < 4.2 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.savefig("tri-together.pdf")
plt.show()

plt.figure(figsize=(10, 10))
plt.subplot(2,1,1)
plt.plot(densityn, flown, 'b', label = 'No control') # plotting t, a separately 
plt.plot(densityd, flowd, 'r', label = 'Dedicated Lane Control') # plotting t, b separately 
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,1,2)
plt.scatter(densityn, flown, color = 'b', s=6, marker = "v", label = 'No control') # plotting t, a separately 
plt.scatter(densityd, flowd, color = 'r', s=6, marker = ">", label = 'Dedicated Lane Control') # plotting t, b separately 
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.savefig("nc-d-together.pdf")
plt.show()

plt.figure(figsize=(10, 10))
plt.subplot(2,1,1)
plt.plot(densityn, flown, 'b', label = 'No control') # plotting t, a separately 
plt.plot(densitydy, flowdy, 'g', label = 'Dynamic Lane Control: v < 4.2 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,1,2)
plt.scatter(densityn, flown, color = 'b', s=6, marker = "v", label = 'No control') # plotting t, a separately 
plt.scatter(densitydy, flowdy, color = 'g', s=6, marker = "<", label = 'Dynamic Lane Control: v < 4.2 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.savefig("nc-dyn-together.pdf")
plt.show()



plt.figure(figsize=(10, 10))
plt.subplot(2,1,1)
plt.plot(densityd, flowd, 'r', label = 'Dedicated Lane Control') # plotting t, b separately 
plt.plot(densitydy, flowdy, 'g', label = 'Dynamic Lane Control: v < 4.2 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,1,2)
plt.scatter(densityd, flowd, color = 'r', s=6, marker = ">", label = 'Dedicated Lane Control') # plotting t, b separately 
plt.scatter(densitydy, flowdy, color = 'g', s=6, marker = "<", label = 'Dynamic Lane Control: v < 4.2 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.savefig("d-dyn-together.pdf")
plt.show()












plt.figure(figsize=(30, 15))
plt.subplot(2,3,1)
plt.plot(densityn, flown, 'b', label = 'No control') # plotting t, a separately 
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,3,2)
plt.plot(densityd, flowd, 'r', label = 'Dedicated Lane Control') # plotting t, b separately 
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,3,3)
plt.plot(densitydy, flowdy, 'g', label = 'Dynamic Lane Control: v < 2 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,3,4)
plt.scatter(densityn, flown, color = 'b', s=1, marker = "o", label = 'No control') # plotting t, a separately 
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,3,5)
plt.scatter(densityd, flowd, color = 'r', s=1, marker = "o", label = 'Dedicated Lane Control') # plotting t, b separately 
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.subplot(2,3,6)
plt.scatter(densitydy, flowdy, color = 'g', s=1, marker = "o", label = 'Dynamic Lane Control: v < 4.2 AV > 30%') # plotting t, b separately plt.xlabel('density')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental Diagram')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig("lineanddotall.pdf")
plt.show()


f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True, figsize = (10, 10) )
ax1.scatter(densityn, flown, color = 'b', s=1, marker = "o", label = 'No control') # plotting t, a separately 
ax1.set_title('Fundamental Diagram')
ax2.scatter(densityd, flowd, color = 'r', s=1, marker = "o", label = 'Dedicated Lane Control') # plotting t, b separately 
ax3.scatter(densitydy, flowdy, color = 'g', s=1, marker = "o", label = 'Dynamic Lane Control: v < 4.2 AV > 30%') # 
f.subplots_adjust(hspace=0)
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
ax3.legend(loc='upper right')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig("columndot.pdf")
plt.show()


f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True, figsize = (10, 10) )
ax1.plot(densityn, flown, 'b', label = 'No control') # plotting t, a separately 
ax1.set_title('Fundamental Diagram')
ax2.plot(densityd, flowd, 'r', label = 'Dedicated Lane Control') # plotting t, b separately 
ax3.plot(densitydy, flowdy, 'g', label = 'Dynamic Lane Control: v < 4.2 AV > 30%') # plotting t, b separately plt.xlabel('density')
f.subplots_adjust(hspace=0)
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
ax3.legend(loc='upper right')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig("columnline.pdf")
plt.show()