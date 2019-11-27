# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:03:20 2019

@author: Owner
"""
from mpl_toolkits.mplot3d import Axes3D
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit
import random 
from astropy import modeling
from PyPDF2 import PdfFileMerger


            #input file: raw data: case_letter + info.txt e.g. dinfo.txt for dedicated case  
            #output file: dyout2.txt
                                       #process 2:  

fn = 'r1m1a.txt'
fr = 'dyout2.txt'
datalose = 29                       #data retain
dnewdata = "dnew line"
with open(fn, 'r') as f:
    lines = f.read().split('\n')
    #to delete line use "del lines[4]"
    #to replace line:
    for i in range(0,len(lines)):    
        if (i % 100)  == 0 or (i % 100) < datalose and i > 0:  #or (i % 4)  == 1 :
            lines[i] = dnewdata
with open(fr,'w') as f:
    f.write('\n'.join(lines))

with open(fr, "r") as f:
    lines = f.readlines()
with open(fr, "w") as f:
    for line in lines:
        if line.strip("\n") != "dnew line":
            f.write(line)
            
with open(r"dyout2.txt", "r+") as f:
    a = f.read()

with open(r"dyout2.txt", "w+") as f:
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
        
with open('dyout2.txt','r') as csvfile:
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

avthresh = 15                                    #control prop of AV
vthresh = 1.5                                      #control v

for element in range(len(updates)):
    avpropcons.append(avthresh)                    
    conspeed.append(vthresh)                                              
    
#print(updates)    

                                #fig names
fig1 = "v5/dy/trigcondvsse.pdf"    
fig2 = "v5/dy/trigcondavsse.pdf"
fig3 = "v5/dy/lcratesse.pdf"
fig4 = "v5/dy/numlanesse.pdf"
fig5 = "v5/dy/trigstatussse.pdf"
fig6 = "v5/dy/fddatasse.pdf"
fig7 = "v5/dy/newflowfdsse.pdf"
fig8 = "v5/dy/fd-rvsse.pdf"
fig9 = "v5/dy/fd-avsse.pdf"
fig10 = "v5/dy/fdfitsse.pdf"
fig11 = "v5/dy/rhovsse.pdf"
fig12 = "v5/dy/summary/resultdssev=1-5av15.pdf"
fig13 = "v5/dy/fdfitrvsse.pdf"
fig14 = "v5/dy/fdfitavsse.pdf"
                                #graph labels

str1 = "Dynamic: v < " + str(vthresh) + " AV > " + str(avthresh)
str2 = "Dedicated " 
str3 = "No Control"


                                    #plotting start
                 #trigger condition: velocity                                                       
plt.plot(updates, cspeed, label = 'data')
plt.plot(updates, conspeed, label = 'threshold control speed')  #turn on for dynamic
plt.legend()
plt.title("Trigger Condition: velocity")
plt.ylabel('Control Speed')
plt.xlabel('Time')
#plt.text(2500,3.05,'control speed')
plt.savefig(fig1)
plt.show()
          
                   #trigger condition: av prop                   

plt.plot(updates, avprop, label = 'data')
#plt.plot(np.unique(updates), np.poly1d(np.polyfit(updates, avprop, 1))(np.unique(updates)))
plt.plot(updates, avpropcons, label = 'threshold percentage') #turn on for dynamic
plt.legend()
#plt.text(0,30.5,'control AV proportion')
plt.title("Trigger Condition: AV Proportion")
plt.ylabel('Proportion of AV (%)')
plt.xlabel('Time')
plt.savefig(fig2)
plt.show()

                         #lane change rate data and fit                  

fitter = modeling.fitting.LevMarLSQFitter()
model = modeling.models.Gaussian1D()   # depending on the data you need to give some initial values
fitted_model = fitter(model, tp, lr)
plt.plot(tp, fitted_model(tp), label='fit')
plt.plot(tp, lr, 'r:', label='data')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Lane Change Rate')
plt.savefig(fig3)
plt.show()

                                    # num lane changes 

plt.plot(updates,lan)
plt.xlabel('time')
plt.ylabel('number of lane changes')
plt.title('Number of lane changes')
plt.savefig(fig4)
plt.show()

                                    #Binary Trigger signal 
plt.plot(updates,trigbin, 'b')
plt.xlabel('time')
plt.ylabel('Trigger status')
plt.savefig(fig5)
plt.show()


                                # Fundamental Diagram : scatter data
plt.scatter(density,flow, color = 'b', s=1, marker = "o")
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental diagram: ' + str3)
plt.savefig(fig6)
plt.show()
                        # Fundamental Diagram : scatter data experimental new flow eqn
plt.scatter(density,newflow, color = 'b', s=1, marker = "o")
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental diagram: ' + str3)
plt.savefig(fig7)
plt.show()  

''' still need to fit the following fds '''
                        # Fundamental Diagram : scatter data rv
plt.scatter(densityrv,flowrv, color = 'b', s=1, marker = "o")
plt.xlabel('density')
plt.ylabel('flow')
plt.title('RV Fundamental diagram: ' + str3)
plt.savefig(fig8)
plt.show()
                    # Fundamental Diagram : scatter data av
plt.scatter(densityav,flowav , color = 'b', s=1, marker = "o")
plt.xlabel('density')
plt.ylabel('flow')
plt.title('AV Fundamental diagram: ' + str3)
plt.savefig(fig9)
plt.show()
                        #piecewise linear curve fitting functions
x = density
y = flow

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])

p0 = [np.mean(x), np.mean(y), 1, 1]

p , e = optimize.curve_fit(piecewise_linear, x, y, p0)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
xd = np.linspace(0, 1, 3000)
#plt.plot(x, y, "o")
plt.plot(xd, piecewise_linear(xd, *p), 'orange', label = 'fit')
plt.scatter(x,y,color = 'mediumblue', s=3, marker = ".", label = str(99 - datalose)+'% data')
plt.legend()
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental diagram: ' + str3)
plt.savefig(fig10)
plt.show()

                                                #RV FD FIT

xrv = densityrv
yrv= flowrv

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])

p0 = [np.mean(xrv), np.mean(yrv), 1, 1]

prv , e = optimize.curve_fit(piecewise_linear, xrv, yrv, p0)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
xdrv = np.linspace(0, max(xrv), 3000)
#plt.plot(x, y, "o")
plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'orange', label = 'fit')
plt.scatter(xrv,yrv,color = 'mediumblue', s=3, marker = ".", label = str(99 - datalose)+'% data')
plt.legend()
plt.xlabel('density')
plt.ylabel('flow')
plt.title('RV Fundamental diagram: ' + str3)
plt.savefig(fig13)
plt.show()

                                                #AV FD FIT

xav = densityav
yav= flowav

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])

p0 = [np.mean(xav), np.mean(yav), 1, 1]

pav , e = optimize.curve_fit(piecewise_linear, xav, yav, p0)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
xdav = np.linspace(0, max(xav), 3000)
#plt.plot(x, y, "o")
plt.plot(xdav, piecewise_linear(xdav, *pav), 'orange', label = 'fit')
plt.scatter(xav,yav,color = 'mediumblue', s=3, marker = ".", label = str(99 - datalose)+'% data')
plt.legend()
plt.xlabel('density')
plt.ylabel('flow')
plt.title('AV Fundamental diagram: ' + str3)
plt.savefig(fig14)
plt.show()


#os.system('python tests.py') #executes plot.py

def model_func(x, a, k, b):
    return a * np.exp(-k*x) + b

# sample data
x = density
y = avgspeed

# curve fit
p0 = (1.,1.e-5,1.) # starting search koefs
opt, pcov = curve_fit(model_func, x, y, p0)
a, k, b = opt
# test result
x2 = np.linspace(0, 1, 3000)
y2 = model_func(x2, a, k, b)
fig, ax = plt.subplots()
ax.plot(x2, y2, color='r', label='Fit. func: $f(x) = %.3f e^{%.3f x} %+.3f$' % (a,k,b))
ax.plot(x, y, 'bo', label='data')
ax.legend(loc='best')
plt.xlabel('density')
plt.ylabel('Speed')
plt.title('Density Speed Relation')
plt.savefig(fig11)
plt.show()



pdfs = [fig1, fig2, fig3, fig4,fig5, fig6,fig7, fig8,fig9, fig10,fig11, fig13, fig14 ]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(fig12)
merger.close()















































'''
fn = 'dinfo.txt'
#dnewdata = "0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "
dnewdata = "dnew line"
with open('dinfo.txt', 'r') as f:
    lines = f.read().split('\n')
    #to delete line use "del lines[4]"
    #to replace line:
    for i in range(0,len(lines)):    
        if (i % 100)  == 0 or (i % 100) < 19 and i > 0:  #or (i % 4)  == 1 :
            lines[i] = dnewdata
with open('dnew.txt','w') as f:
    f.write('\n'.join(lines))

with open("dnew.txt", "r") as f:
    lines = f.readlines()
with open("dnew.txt", "w") as f:
    for line in lines:
        if line.strip("\n") != "dnew line":
            f.write(line)
            
with open(r"dnew.txt", "r+") as f:
    a = f.read()

with open(r"dnew.txt", "w+") as f:
        f.write("0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  \n" + a)
'''



'''
x = np.linspace(0, 10, 100)
y = 10*x + 2 ** random.randint(5, 15)


lines_seen = set() # holds lines already seen
outfile = open("tout.txt", "w")
for line in open("txt.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

with open(r"txt.txt", "r+") as f:
    a = f.read()
   # print(a)
#Now writing into the file with the prepend line + old file data
    with open(r"txt.txt", "w+") as f:
        f.write("0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  \n" + a)
        #below code to verify the data in the file
        with open(r"txt.txt", "r+") as f:
            b = f.read()
            print(b)
with open("txt.txt", "r") as infile:
    lines = infile.readlines()

i = 6

with open("txt.txt", "w") as outfile:
    for pos, line in enumerate(lines):
        if line.strip("\n") != '6':
            outfile.write(line)
        print("Line number " + str(pos) +" contains: " + str(line))


fn = 'txt.txt'
dnewdata = "0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "
with open('dyout.txt', 'r') as f:
    lines = f.read().split('\n')
    #to delete line use "del lines[4]"
    #to replace line:
    for i in range(0,len(lines)):    
        if (i % 4)  == 0  or (i % 4)  == 1 :
            lines[i] = dnewdata
with open(fn,'w') as f:
    f.write('\n'.join(lines))
          
lines_seen = set() # holds lines already seen
outfile = open("txtfinal.txt", "w")
for line in open("txt.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()    

'''

'''                             #process 1
fn = 'dinfo.txt'
#dnewdata = "0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "
dnewdata = "dnew line"
with open('dinfo.txt', 'r') as f:
    lines = f.read().split('\n')
    #to delete line use "del lines[4]"
    #to replace line:
    for i in range(0,len(lines)):    
        if (i % 100)  == 0 and i > 0:# or (i % 100) < 79 and i > 0:  #or (i % 4)  == 1 :
            lines[i] = dnewdata
with open('dnew.txt','w') as f:
    f.write('\n'.join(lines))

with open("dnew.txt", "r") as f:
    lines = f.readlines()
with open("dnew.txt", "w") as f:
    for line in lines:
        if line.strip("\n") != "dnew line":
            f.write(line)
            
with open(r"dnew.txt", "r+") as f:
    a = f.read()

with open(r"dnew.txt", "w+") as f:
        f.write("0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  \n" + a)
'''
