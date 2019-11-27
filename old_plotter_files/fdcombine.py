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
import glob



filenames_dd = sorted(glob.glob('fdd*.txt'))
filenames_nc = sorted(glob.glob('fdno*.txt'))

density1= density2= density3= density4 = []
flow1= flow2= flow3= flow4 = []
updates1= updates2= updates3= updates4 = []
densityrv1= densityrv2= densityrv3= densityrv4 = []
flowrv1= flowrv2= flowrv3= flowrv4 = []
densityav1= densityav2= densityav3= densityav4 = []
flowav1= flowav2= flowav3= flowav4 = []



density = [density1, density2, density3, density4]
flow = [flow1, flow2, flow3, flow4]
updates = [updates1, updates2, updates3, updates4]
densityrv = [densityrv1, densityrv2, densityrv3, densityrv4]
flowrv = [flowrv1, flowrv2, flowrv3, flowrv4]
densityav = [densityav1, densityav2, densityav3, densityav4]
flowav = [flowav1, flowav2, flowav3, flowav4]



for f in filenames_dd:
    for i in range(0,4):  
        with open(f,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                density[i].append(float(row[0]))
                flow[i].append(float(row[1]))
                updates[i].append(float(row[2]))
                densityrv[i].append(float(row[3]))
                flowrv[i].append(float(row[4]))
                densityav[i].append(float(row[5]))
                flowav[i].append(float(row[6]))
                
#1,2,3,4 ---> %
#5,6,7 ---> total, rv, av
            
for k in range(1,5):
    for m in range(5,8):
        exec(f'x_{k}_{m} = 0')
        exec(f'y_{k}_{m} = 0')
        exec(f'p0_{k}_{m} = 0')
        exec(f'y_weight_{k}_{m} = 0')
        exec(f'flow_max_index_{k}_{m} = 0')    
        exec(f'p_{k}_{m} = 0')
        exec(f'y_crit_{k}_{m} = 0')
        exec(f'x_crit_{k}_{m} = 0')
        exec(f'x_jam_{k}_{m} = 0')
        exec(f'free_y_{k}_{m} = 0')
        exec(f'wave_v_{k}_{m} = 0')



