# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:51:36 2019

@author: Owner
"""

from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit
from PyPDF2 import PdfFileMerger


#density , flow, updates, numlane, avgspeed
densityn = []
flown = []
updates = []
lan = []
avgspeedn = []
trigbinn = []
cspeedn = []
count1n = 0
count2n = 0
avpropn = []
newflown = []
densityrvn = []
flowrvn = []
densityavn = []
flowavn = []  

with open('nout2.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        densityn.append(float(row[0]))
        flown.append(float(row[1]))
        updates.append(float(row[2]))
        lan.append(float(row[3]))
        avgspeedn.append(float(row[4]))
        trigbinn.append(float(row[5]))        
        cspeedn.append(float(row[6]))
        avpropn.append(float(row[7]))
        newflown.append(float(row[8]))
        densityrvn.append(float(row[9]))
        flowrvn.append(float(row[10]))
        densityavn.append(float(row[11]))
        flowavn.append(float(row[12]))

xn = densityn
yn = flown


#x = np.array([7228,7620,7730,7901,8139,8370,8448,8737,8824,9089,9233,9321,9509,9568,9642,9756,9915,10601,10942], dtype=np.float)
#y= np.array([.874,.893,.8905,.8916,.9095,.9142,.9109,.9185,.9169,.9251,.9290,.9304,.9467,.9378,0.9464,0.9508,0.9583,0.9857,0.9975],dtype=np.float)

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])


p0 = [np.mean(xn), np.mean(yn), 1, 1]

pn , e = optimize.curve_fit(piecewise_linear, xn, yn, p0)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
xd = np.linspace(0, 1, 3000)
#plt.plot(x, y, "o")
plt.plot(xd, piecewise_linear(xd, *pn), label = 'No Control')
plt.legend()



print("no control: \n"  + "density at max flow: " +str(pn[0]) + " max flow: " + str(pn[1]))  # [  9.32099947e+03   9.32965835e-01   2.58225121e-05   4.05400820e-05]
#print(np.diag(e))  

fig1 = "1.pdf"
fig2 = "2.pdf"
fig3 = "3.pdf"

densitydd = []
flowdd = []
updates = []
lan = []
avgspeeddd = []
trigbindd = []
cspeeddd = []
count1dd = 0
count2dd = 0
avpropdd = []
newflowdd = []
densityrvdd = []
flowrvdd = []
densityavdd = []
flowavdd = []  

with open('dout2.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        densitydd.append(float(row[0]))
        flowdd.append(float(row[1]))
        updates.append(float(row[2]))
        lan.append(float(row[3]))
        avgspeeddd.append(float(row[4]))
        trigbindd.append(float(row[5]))        
        cspeeddd.append(float(row[6]))
        avpropdd.append(float(row[7]))
        newflowdd.append(float(row[8]))
        densityrvdd.append(float(row[9]))
        flowrvdd.append(float(row[10]))
        densityavdd.append(float(row[11]))
        flowavdd.append(float(row[12]))

xdd = densitydd
ydd = flowdd


#x = np.array([7228,7620,7730,7901,8139,8370,8448,8737,8824,9089,9233,9321,9509,9568,9642,9756,9915,10601,10942], dtype=np.float)
#y= np.array([.874,.893,.8905,.8916,.9095,.9142,.9109,.9185,.9169,.9251,.9290,.9304,.9467,.9378,0.9464,0.9508,0.9583,0.9857,0.9975],dtype=np.float)

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])


p0 = [np.mean(xdd), np.mean(ydd), 1, 1]

pdd , e = optimize.curve_fit(piecewise_linear, xdd, ydd, p0)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
xd = np.linspace(0, 1, 3000)
#plt.plot(x, y, "o")
plt.plot(xd, piecewise_linear(xd, *pdd), label = 'Dedicated')
plt.legend()

print("dedicated: \n" + "density at max flow: " +str(pdd[0]) + " max flow: " + str(pdd[1]))  # [  9.32099947e+03   9.32965835e-01   2.58225121e-05   4.05400820e-05]
#print(np.diag(e))  


densitydy = []
flowdy = []
updates = []
lan = []
avgspeeddy = []
trigbindy = []
cspeeddy = []
count1dy = 0
count2dy = 0
avpropdy = []
newflowdy = []
densityrvdy = []
flowrvdy = []
densityavdy = []
flowavdy = []  

with open('dyout2.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        densitydy.append(float(row[0]))
        flowdy.append(float(row[1]))
        updates.append(float(row[2]))
        lan.append(float(row[3]))
        avgspeeddy.append(float(row[4]))
        trigbindy.append(float(row[5]))        
        cspeeddy.append(float(row[6]))
        avpropdy.append(float(row[7]))
        newflowdy.append(float(row[8]))
        densityrvdy.append(float(row[9]))
        flowrvdy.append(float(row[10]))
        densityavdy.append(float(row[11]))
        flowavdy.append(float(row[12]))

xdy = densitydy
ydy = flowdy


#x = np.array([7228,7620,7730,7901,8139,8370,8448,8737,8824,9089,9233,9321,9509,9568,9642,9756,9915,10601,10942], dtype=np.float)
#y= np.array([.874,.893,.8905,.8916,.9095,.9142,.9109,.9185,.9169,.9251,.9290,.9304,.9467,.9378,0.9464,0.9508,0.9583,0.9857,0.9975],dtype=np.float)

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])


p0 = [np.mean(xdy), np.mean(ydy), 1, 1]

pdy , e = optimize.curve_fit(piecewise_linear, xdy, ydy, p0)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
xd = np.linspace(0, 1, 3000)
#plt.plot(x, y, "o")
plt.plot(xd, piecewise_linear(xd, *pdy), label = 'Dynamic:v < 2.5 AV > 5%')
plt.legend()
plt.xlabel('Density')
plt.ylabel('Flow')
plt.title('Normalized Fundamental Diagram')
plt.savefig(fig1)
print("dynamic: \n" + "density at max flow: " +str(pdy[0]) + " max flow: " + str(pdy[1]))  # [  9.32099947e+03   9.32965835e-01   2.58225121e-05   4.05400820e-05]
#print(np.diag(e))  


fig = plt.figure(figsize=(8, 10))

sub1 = fig.add_subplot(311)
sub1.plot(xd, piecewise_linear(xd, *pn), 'orange',label = 'No Control')
sub1.scatter(xn,yn,color = 'mediumblue', s=3, marker = ".", label = 'data')
sub1.set_title('Normalized Fundamental Diagram')
plt.legend()

sub2 = fig.add_subplot(312)
sub2.plot(xd, piecewise_linear(xd, *pdd), 'r', label = 'Dedicated')
sub2.scatter(xdd,ydd,color = 'mediumblue', s=3, marker = ".", label = 'data')
sub2.set_title('Normalized Fundamental Diagram')
plt.legend()

sub3 = fig.add_subplot(313)
sub3.plot(xd, piecewise_linear(xd, *pdy),'g' ,label = 'Dynamic: v < 2.5 AV > 5%')
sub3.scatter(xdy,ydy,color = 'mediumblue', s=3, marker = ".", label = 'data')
sub3.set_title('Normalized Fundamental Diagram')
plt.legend()
plt.savefig(fig2)
plt.show() 


def model_func(x, a, k, b):
    return a * np.exp(-k*x) + b

# sample data
x = densityn
y = avgspeedn

# curve fit
p0 = (1.,1.e-5,1.) # starting search koefs
opt, pcov = curve_fit(model_func, x, y, p0)
a, k, b = opt
# test result
x2 = np.linspace(0, 1, 3000)
y2 = model_func(x2, a, k, b)

x = densitydy
y = avgspeeddy

p0 = (1.,1.e-5,1.) # starting search koefs
opt, pcov = curve_fit(model_func, x, y, p0)
a, k, b = opt
# test result
x1 = np.linspace(0, 1, 3000)
y1 = model_func(x2, a, k, b)

x = densitydd
y = avgspeeddd

p0 = (1.,1.e-5,1.) # starting search koefs
opt, pcov = curve_fit(model_func, x, y, p0)
a, k, b = opt
# test result
x3 = np.linspace(0, 1, 3000)
y3 = model_func(x2, a, k, b)


fig, ax = plt.subplots()
ax.plot(x1, y1, color='r', label='dynamic' )
ax.plot(x3, y3, color='g', label='dedicated')
ax.plot(x2, y2, color='b', label='no control')
ax.legend(loc='best')
plt.xlabel('density')
plt.ylabel('Speed')
plt.title('Density Speed Relation')
plt.savefig(fig3)
plt.show()


''' Provision for lane change rate compare'''

fig4 = "4.pdf"

x1 = densityrvn
y1 = flowrvn

p01 = [np.mean(x1), np.mean(y1), 1, 1]

p1 , e = optimize.curve_fit(piecewise_linear, x1, y1, p01)  # set initial parameter estimates
perr1 = np.sqrt(np.diag(e))
xd1 = np.linspace(0, max(x1), 3000)

x2 = densityrvdd
y2 = flowrvdd

p02 = [np.mean(x2), np.mean(y2), 1, 1]

p2 , e = optimize.curve_fit(piecewise_linear, x2, y2, p02)  # set initial parameter estimates
perr2 = np.sqrt(np.diag(e))
xd2 = np.linspace(0, max(x2), 3000)

x3 = densityrvdy
y3 = flowrvdy

p03 = [np.mean(x3), np.mean(y3), 1, 1]

p3 , e = optimize.curve_fit(piecewise_linear, x3, y3, p03)  # set initial parameter estimates
perr3 = np.sqrt(np.diag(e))
xd3 = np.linspace(0, max(x3), 3000)


fig, ax = plt.subplots()
ax.plot(xd3, piecewise_linear(xd3, *p3), color='r', label='dynamic' )
ax.plot(xd2, piecewise_linear(xd2, *p2), color='g', label='dedicated')
ax.plot(xd1, piecewise_linear(xd1, *p1), color='b', label='no control')
ax.legend(loc='best')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('RV Fundamental Diagram')
plt.savefig(fig4)
plt.show()


fig5 = "5.pdf"

x1 = densityavn
y1 = flowavn

p01 = [np.mean(x1), np.mean(y1), 1, 1]

p1 , e = optimize.curve_fit(piecewise_linear, x1, y1, p01)  # set initial parameter estimates
perr1 = np.sqrt(np.diag(e))
xd1 = np.linspace(0, max(x1), 3000)

x2 = densityavdd
y2 = flowavdd

p02 = [np.mean(x2), np.mean(y2), 1, 1]

p2 , e = optimize.curve_fit(piecewise_linear, x2, y2, p02)  # set initial parameter estimates
perr2 = np.sqrt(np.diag(e))
xd2 = np.linspace(0, max(x2), 3000)

x3 = densityavdy
y3 = flowavdy

p03 = [np.mean(x3), np.mean(y3), 1, 1]

p3 , e = optimize.curve_fit(piecewise_linear, x3, y3, p03)  # set initial parameter estimates
perr3 = np.sqrt(np.diag(e))
xd3 = np.linspace(0, max(x3), 3000)


fig, ax = plt.subplots()
ax.plot(xd3, piecewise_linear(xd3, *p3), color='r', label='dynamic' )
ax.plot(xd2, piecewise_linear(xd2, *p2), color='g', label='dedicated')
ax.plot(xd1, piecewise_linear(xd1, *p1), color='b', label='no control')
ax.legend(loc='best')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('AV Fundamental Diagram')
plt.savefig(fig5)
plt.show()

pdfs = [fig1, fig2, fig3, fig4, fig5 ]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("v5datalosscombinedv=15av=15.pdf")
merger.close()