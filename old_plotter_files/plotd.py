# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:52:16 2019

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 18:31:10 2019

@author: Owner
"""
import pylab
from mpl_toolkits.mplot3d import Axes3D
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
fn = 'dinfo.txt'
fr = 'dout1.txt'
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
            
with open(r"dout1.txt", "r+") as f:     #fr change
    a = f.read()

with open(r"dout1.txt", "w+") as f:     #fr change
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
        
with open('dout1.txt','r') as csvfile:
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

avthresh = 15                                 #control prop of AV
vthresh = 3                                   #control v

for element in range(len(updates)):
    avpropcons.append(avthresh)                    
    conspeed.append(vthresh)                                              
    
#print(updates)    

                                #fig names
fig1 = "v6/d/trigcondv.pdf"    
fig2 = "v6/d/trigcondav.pdf"
fig3 = "v6/d/lcrate.pdf"
fig4 = "v6/d/numlane.pdf"
fig5 = "v6/d/trigstatus.pdf"
fig6 = "v6/d/fddata.pdf"
fig7 = "v6/d/newflowfd.pdf"
fig8 = "v6/d/fd-rv.pdf"
fig9 = "v6/d/fd-av.pdf"
fig10 = "v6/d/fdfit.pdf"
fig11 = "v6/d/rhov.pdf"
fig12 = "v6/d/summary/result-dd-av_"+str(avthresh)+".pdf"
fig13 = "v6/d/fdfitrv.pdf"
fig14 = "v6/d/fdfitav.pdf"
fig15 = "v6/d/drvdav.pdf"
fig16 = "v6/d/fdrvav.pdf"                       
#fig17 = "v6/d/3dscatter.pdf"        
#fig18 = "v6/d/3dcontour.pdf"       
#fig19 = "v6/d/3dsurface.pdf"                       
fig20 = "v6/d/flowrv.pdf"     
fig21 = "v6/d/flowav.pdf"               
fig22 = "v6/d/flowavrv.pdf"         
fig23 = "v6/d/fdall.pdf"               
      
                      #graph labels

str1 = "Dynamic: v < " + str(vthresh) + " AV > " + str(avthresh)
str2 = "Dedicated: AV ~ " +str(avthresh) + "%" 
str2 = "No Control"
                                #flow analysis:
'''
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
#ax.plt.savefg(fig17)
# Example points that use a color proportional to the radial distance

X = x_line
Y = y_line
Z = z_line

pylab.scatter(X,Y,c=Z,linewidths=.01)
pylab.axis('equal')
#pylab.show()

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
plt.savefig(fig19)
plt.show()

'''

plt.scatter(flowrv, flow, s= 1)
plt.xlabel("RV flow")
plt.ylabel("Overall flow")
plt.title("Overall flow vs RV flow")
#plt.legend()
plt.savefig(fig20)
plt.show()

plt.scatter(flowav, flow, s= 1)
plt.xlabel("AV flow")
plt.ylabel("Overall flow")
plt.title("Overall flow vs AV flow")
plt.savefig(fig21)
#plt.legend()
plt.show()


plt.scatter(flowrv, flowav, s= 1)
plt.xlabel("RV flow")
plt.ylabel("AV flow")
plt.title("RV flow vs AV flow")
plt.savefig(fig22)
#plt.legend()
plt.show()                                    #plotting start
                 #trigger condition: velocity                                                       
plt.plot(updates, cspeed, label = 'data')
#plt.plot(updates, conspeed, label = 'threshold control speed')
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
#plt.plot(updates, avpropcons, label = 'threshold percentage')
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
plt.title('Fundamental diagram: ' + str2)
plt.savefig(fig6)
plt.show()
                        # Fundamental Diagram : scatter data experimental new flow eqn
plt.scatter(density,newflow, color = 'b', s=1, marker = "o")
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental diagram: ' + str2)
#plt.savefig(fig7)
plt.show()  

                        # Fundamental Diagram : scatter data rv
plt.scatter(densityrv,flowrv, color = 'b', s=1, marker = "o")
plt.xlabel('density')
plt.ylabel('flow')
plt.title('RV Fundamental diagram: ' + str2)
plt.savefig(fig8)
plt.show()
                    # Fundamental Diagram : scatter data av
plt.scatter(densityav,flowav , color = 'b', s=1, marker = "o")
plt.xlabel('density')
plt.ylabel('flow')
plt.title('AV Fundamental diagram: ' + str2)
plt.savefig(fig9)
plt.show()
                                #piecewise linear curve fitting function and plot
x = density
y = flow

N = 3000


def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])

p0 = [np.mean(x), np.mean(y), 1, 1]
            #weighing functions:            
            
y_weight = np.empty(len(y))
y_weight.fill(10)
y_weight[0] = y_weight[-5:-1] = 0.1



p , e = optimize.curve_fit(piecewise_linear, x, y, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
xd = np.linspace(0, 1, N)
#plt.plot(x, y, "o")
plt.plot(xd, piecewise_linear(xd, *p), 'orange', label = 'fit')
plt.scatter(x,y,color = 'mediumblue', s=3, marker = ".", label = 'data')
plt.legend()
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental diagram: ' + str2)
plt.savefig(fig10)
plt.show()


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



prv , e = optimize.curve_fit(piecewise_linear, xrv, yrv, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
xdrv = np.linspace(0, max(xrv), 3000)
#plt.plot(x, y, "o")
plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'orange', label = 'fit')
plt.scatter(xrv,yrv,color = 'mediumblue', s=3, marker = ".", label = 'data')
plt.legend()
plt.xlabel('density')
plt.ylabel('flow')
plt.title('RV Fundamental diagram: ' + str2)
plt.savefig(fig13)
plt.show()

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
y_weight[0] = 0.1


pav , e = optimize.curve_fit(piecewise_linear, xav, yav, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
perr = np.sqrt(np.diag(e))
xdav = np.linspace(0, max(xav), 3000)
#plt.plot(x, y, "o")
plt.plot(xdav, piecewise_linear(xdav, *pav), 'orange', label = 'fit')
plt.scatter(xav,yav,color = 'mediumblue', s=3, marker = ".", label = 'data')
plt.legend()
plt.xlabel('density')
plt.ylabel('flow')
plt.title('AV Fundamental diagram: ' + str2)
plt.savefig(fig14)
plt.show()

                                            #density RV - density AV

plt.plot(xdav, xdrv, label = str2)
plt.xlabel('Density of AV')
plt.ylabel('Density of RV')
plt.title('Mixed flow density relationship: ')
#plt.legend(loc='best')
plt.savefig(fig15)
plt.show()


                                                    #FD RV FD AV

plt.plot(xdav, piecewise_linear(xdav, *pav), 'red', label = 'AV')
plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'blue', label = 'RV')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental diagram: ' + str2)
plt.legend()
plt.savefig(fig16)
plt.show()

                                                    #FD ALL

plt.plot(xdav, piecewise_linear(xdav, *pav), 'red', label = 'AV')
plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'blue', label = 'RV')
plt.plot(xd, piecewise_linear(xd, *p), 'orange', label = 'Overall')
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental diagram: ' + str2)
plt.legend()
plt.savefig(fig23)
plt.show()


                                    #fitting density velocity graph
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
ax.scatter(x, y, s=3,label='data')
ax.legend(loc='best')
plt.xlabel('density')
plt.ylabel('Speed')
plt.title('Density Speed Relation')
plt.savefig(fig11)
plt.show()

                                            #merging pdfs into one

pdfs = [fig1, fig2, fig3, fig4,fig5, fig6, fig8,fig9, fig10,fig11, fig13, fig14, fig15, fig16, fig20, fig21, fig22, fig23 ]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(fig12)
merger.close()



























'''
x = density
y = flow

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])

p , e = optimize.curve_fit(piecewise_linear, x, y)
xd = np.linspace(0, 1, 1000)
plt.plot(x, y, ".")
plt.plot(xd, piecewise_linear(xd, *p))
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental diagram: Dynamic: v < 3 and AV prop > 30%')
#plt.savefig("fdtri.pdf")
plt.show()
p , e = optimize.curve_fit(piecewise_linear, x, y)
xd = np.linspace(0, 1, 1000)
#plt.plot(x, y, ".")
plt.plot(xd, piecewise_linear(xd, *p))
plt.xlabel('density')
plt.ylabel('flow')
plt.title('Fundamental diagram: Dynamic: v < 3 and AV prop > 30%')
#plt.savefig("triangularfd.pdf")
plt.show()
'''
#os.system('python fit.py') #executes plot.py
'''

#  tests v
plt.plot(updates,density, 'b')
plt.ylabel('density')
plt.xlabel('time')
plt.show()

plt.plot(updates, flow,'b')
plt.ylabel('flow')
plt.xlabel('time')
plt.show()

plt.plot(updates, avgspeed, 'b')
plt.ylabel('speed')
plt.xlabel('time')
plt.show()

plt.scatter(flow, lan, color = 'b', s=1, marker = "o")
plt.ylabel('number of lane changes')
plt.xlabel('flow')
plt.show()

plt.scatter(avgspeed, lan, color = 'b', s=1, marker = "o")
plt.ylabel('number of lane changes')
plt.xlabel('speed')
plt.show()

fig = plt.figure(figsize=(12, 10))
sub1 = fig.add_subplot(221)
sub1.set_title('Fundamental diagram: Dynamic - velocity < 2 and AV proportion > 30')
sub1.scatter(density, flow, color = 'b', s=1, marker = "o")
sub3 = fig.add_subplot(222)
sub3.set_title('Density Speed Relation')
sub3.scatter(density,avgspeed, color = 'b', s=1, marker = "o")
sub4 = fig.add_subplot(223)
sub4.set_title('Number of Lane changes')
sub4.plot(updates, lan)
sub5 = fig.add_subplot(224)
sub5.set_title('Flow Speed Relation')
sub5.scatter(flow,avgspeed, color = 'b', s=1, marker = "o")
plt.tight_layout()
plt.savefig("combined.pdf")
plt.show()  
             
#tests^

plt.scatter(density,avgspeed, color = 'b', s=1, marker = "o")
plt.xlabel('density')
plt.ylabel('speed')
plt.title('Density Speed Relation')
plt.savefig("denspeedot.pdf")
plt.show()


plt.plot(flow,avgspeed, 'b')
plt.xlabel('flow')
plt.ylabel('Speed')
plt.title('Flow Speed Relation')
plt.savefig("flownspeed.pdf")
plt.show()

plt.scatter(flow,avgspeed, color = 'b', s=1, marker = "o")
plt.xlabel('flow')
plt.ylabel('speed')
plt.title('Flow Speed Relation')
plt.savefig("flowspeedot.pdf")
plt.show()

plt.plot(updates,lan, 'b')
plt.xlabel('time')
plt.ylabel('number of lane changes')
plt.title('Number of lane changes')
plt.savefig("numlane.pdf")
plt.show()

plt.plot(updates,avgspeed, 'b')
plt.xlabel('time')
plt.ylabel('speed')
plt.title('Dynamics')
plt.savefig("speedtime.pdf")
plt.show()

plt.scatter(updates,avgspeed, color = 'b', s=1, marker = "o")
plt.xlabel('time')
plt.ylabel('speed')
plt.title('Dynamics')
plt.savefig("speedtimedot.pdf")
plt.show()
'''