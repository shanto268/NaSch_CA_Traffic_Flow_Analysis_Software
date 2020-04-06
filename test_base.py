# -*- coding: utf-8 -*-
"""
Experiment 2 plot

Note: remove -1 from clusterability

"""

from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import csv
#from scipy.optimize import curve_fit
#from scipy.optimize import differential_evolution
#import warnings

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_ptss
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])
        
def x_intercept(slope, yi, xi):
    return (slope*xi - yi)/ slope

def histo(a,q3,nn):  # a is array, q3 is a string label for parameter name and nn is nn[0]
    a = list(filter(lambda x: x != 0.0, a)) #array with zero remobed
    b = [[x,a.count(x)] for x in set(a)]
    num = []
    freq = []
    
    for i in b:
        num.append(i[0])
        freq.append(i[1])
    
    alphab = num # x axis 
    alphab = np.round(alphab,2)
    alphab.sort()
    
    sum_freq = 0
    sum_numer = 0
    
    for i in range(len(alphab)):
        sum_freq += freq[i]
        sum_numer += (alphab[i]*freq[i])
    
    if sum_freq == 0:
        w_mean = 0
    else:
        w_mean = ( sum_numer / sum_freq )
        
    print("Average of " + str(q3) + " is "  + str(w_mean) + " for " + str(nn) + "\n")
    

def plot1(fname):
        fn = fname
        new_nn = fname.split('/')
        fn = new_nn[3]
        nn = fn.split('.')

        density = []
        flow = []
        updates = []
        densityrv = []
        flowrv = []
        densityav = []
        flowav = []        
        clnum = []
        avgclsize = []
        prob = []        
        totlane = []
        avlane = []
        rvlane = []
        carclus = []
        
        with open(fname,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                density.append(float(row[0]))
                flow.append(float(row[1]))
                updates.append(float(row[2]))
                densityrv.append(float(row[3]))
                flowrv.append(float(row[4]))
                densityav.append(float(row[5]))
                flowav.append(float(row[6]))
                clnum.append(float(row[7]))
                avgclsize.append(float(row[8]))
                prob.append(float(row[9]))
                totlane.append(float(row[10]))
                avlane.append(float(row[11]))
                rvlane.append(float(row[12]))
                carclus.append(float(row[13]))
                
        FD_arr = []
        params = []  #fd, fdrv, fdav
        FD_RV_arr = []
        FD_AV_arr = []
        
        dens = density[::99]
        totlane_dens = totlane[::99]
        avlane_dens = avlane[::99]
        rvlane_dens = rvlane[::99]
        totlane_dens = [totlane_dens[0]] + [totlane_dens[i+1] - totlane_dens[i] for i in range(len(totlane_dens)-1)]
        avlane_dens = [avlane_dens[0]] + [avlane_dens[i+1] - avlane_dens[i] for i in range(len(avlane_dens)-1)]
        rvlane_dens = [rvlane_dens[0]] + [rvlane_dens[i+1] - rvlane_dens[i] for i in range(len(rvlane_dens)-1)]
        
    #    print("av: " + str(avlane_dens))
    #    print("rv: " + str(rvlane_dens))
   #     print("\n\n")
        densityrv_ = densityrv[::99]
        densityav_ = densityav[::99]
        numrv = [round(300*i) for i in densityrv_]
        numav = [round(300*i) for i in densityav_] 
        
   #     print("numav: " + str(numav))
   #     print("numrv: " + str(numrv))
   #     print("\n\n")
        
        for i in range(len(avlane_dens)):
            avlane_dens[i] = avlane_dens[i] / numav[i] 
            rvlane_dens[i] = rvlane_dens[i] / numrv[i] 
            totlane_dens[i] = totlane_dens[i] / (numrv[i] + numav[i] )
      #  print("total: " + str(totlane_dens))
    #    print("av: " + str(avlane_dens))
   #     print("rv: " + str(rvlane_dens))
            
        cum_clnum = []
        cum_i = 0
        for i in clnum:
            cum_i += i
            cum_clnum.append(cum_i)
            
        carclus = list(filter(lambda a: a != -1, carclus))
        
        a = avgclsize
        tcls = []
        index = []
        t = 0
        for i in range(len(a)):
            if a[i] != 0:
                index.append(i)
        t = 0
        for i in range(len(index)-1):
            j = i + 1
            if j <= len(index):
                if (index[j] - index[i]) == 1:
                    t += 1
                    if j == len(index) - 1:
                        tcls.append(t)
                else:
                    tcls.append(t)
                    t = 0
        histo(tcls, "Time period of clusters", nn[0])
        
    
        ####
        
        plt.scatter(dens, totlane_dens, label='Total')
        plt.scatter(dens, avlane_dens, label='AV')
        plt.scatter(dens, rvlane_dens, label='HV')
        plt.plot(dens, totlane_dens)
        plt.plot(dens, avlane_dens)
        plt.plot(dens, rvlane_dens)
        plt.xlabel("System Density")
        plt.ylabel("Lane Change Rate")
        plt.ylim(0,30)
        plt.title("Lane Change Rate " + str(nn[0]))
        plt.legend()
    #    plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/lane_change_rate_all_trials"+str(nn[0])+".png")
        plt.show()        
        
        plt.plot(updates, totlane, 'black', label='Total')
        plt.plot(updates, avlane, 'red', label='AV')
        plt.plot(updates, rvlane, 'blue', label='HV')
        plt.xlabel("Timesteps")
        plt.ylabel("Total Number of Lane Changes")
        plt.title("Number of Lane Changes over time "+ str(nn[0]))
        plt.ylim(0,10000)
        plt.legend()
    #    plt.savefig("draft_2/experiment_2/figures/"+str(nn[0])+"/total_number_of_lane_changes_all_"+str(nn[0])+".png")
        plt.show()
        
        
        return FD_arr, FD_RV_arr, FD_AV_arr, params
        
        
namea = "draft_2/experiment_2/data_files/fd_oppo.txt"
nameb = "draft_2/experiment_2/data_files/fd_aware.txt"
nameba = "draft_2/experiment_2/data_files/fd_aware_oppo.txt"
namec = "draft_2/experiment_2/data_files/fd_base_hvlike.txt"
nameca = "draft_2/experiment_2/data_files/fd_base_hway.txt"         
namecb = "draft_2/experiment_2/data_files/fd_base_hway_base.txt"
#namecc = "draft_2/experiment_2/data_files/fd_base_hvlike_no_elif.txt"


def plotall():
    plot_all = [namea, nameb, nameba, namec, nameca]
    for i in plot_all:
        plot1(i)

plotall()
