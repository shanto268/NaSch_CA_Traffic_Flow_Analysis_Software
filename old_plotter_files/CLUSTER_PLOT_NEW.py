# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:13:35 2019

@author: Owner
"""

import matplotlib.pyplot as plt
import csv

def plot1(fname):
        fn = fname
        nn = fn.split('.')        
        fr = 'processed_' + str(fname) + '.txt'
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
                    
        with open(fn, "r+") as f:     #fr change
            a = f.read()
        
#        with open(fr, "w+") as f:     #fr change
#                f.write("0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  \n" + a)
        
        
        density = []
        flow = []
        updates = []
        densityrv = []
        flowrv = []
        densityav = []
        flowav = []        
        clnum = []
        avgclsize = []
#        clsize = [] 
        
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
                clnum.append(int(row[13]))
                avgclsize.append(float(row[14]))
 #               clsize.append(float(row[11]))

        
        plt.plot(updates, clnum,':' ,linewidth =1, )
        plt.xlabel("Timesteps")
        plt.ylabel("Number of Clusters")
        plt.title("Number of Clusters over time")
        plt.savefig("final/new/cluster_num_"+str(nn[0])+".pdf")
        plt.show()
        
        plt.plot(updates, avgclsize ,linewidth =1,)
        plt.xlabel("Timesteps")
        plt.ylabel("Average Size of Clusters")
        plt.title("Average Size of Clusters over time")
        plt.savefig("final/new/cluster_size_"+str(nn[0])+".pdf")
        plt.show()
        
 
#r1m1 = plot1('type_aware_crit_density.txt')
#r1m2 = plot1('type_unaware_crit_density.txt')
#r2m1 = plot1('control_crit_density.txt')
r = plot1('type_unaware_low_density_same_vf.txt')

#show histograms: 
    #cluster numbers at each time period
    #average size at each time period
    #size 

#combined graphs:              
