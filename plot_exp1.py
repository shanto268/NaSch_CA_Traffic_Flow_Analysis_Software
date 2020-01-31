# -*- coding: utf-8 -*-
"""
Experiment 1 plot

Note: Make ylim consistent
"""
from matplotlib.ticker import StrMethodFormatter
import matplotlib.pyplot as plt
import numpy as np
import csv 


def plot1(fname):
        fn = fname
        new_nn = fname.split('/')
        fn = new_nn[3]
        nn = fn.split('.')
 #       fr = str(nn[0]) + '.txt'
        
        """
        #dnewdata = "0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "
        dnewdata = "dnew line"
        with open(fname, 'r') as f:
            lines = f.read().split('\n')
            #to delete line use "del lines[4]"
            #to replace line:
            for i in range(0,len(lines)):    
                if (i % 100)  == 0 or (i % 100) < 19 and i > 0:  #or (i % 4)  == 1 :
                    lines[i] = dnewdata
        with open(fname,'w') as f:
            f.write('\n'.join(lines))

        with open(fname, "r") as f:
            lines = f.readlines()
        
        with open(fname, "w") as f:
            for line in lines:
                if line.strip("\n") != "dnew line":
                    f.write(line)
                    
        with open(fname, "r+") as f:     #fr change
            a = f.read()
        with open(fr, "w+") as f:     #fr change
                f.write("0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  \n" + a)
        """
        
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
        time = []
        tcls = []
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
                
        for i in range(len(updates)):
            t =  2.2 * updates[i]
            time.append(t)
        
        cum_clnum = []
        cum_i = 0
        for i in clnum:
            cum_i += i
            cum_clnum.append(cum_i)
    
        print(str(nn[0]) + " average clusterability value: " + str(sum(carclus) / len(carclus)) )
        
        plt.plot(updates, totlane, 'black', label='Total')
        plt.plot(updates, avlane, 'red', label='AV')
        plt.plot(updates, rvlane, 'blue', label='RV')
        plt.xlabel("Timesteps")
        plt.ylabel("Total Number of Lane Changes")
     #   plt.ylim(0,7000)
        plt.title("Number of Lane Changes over time")
        plt.legend()
        plt.savefig("draft_2/experiment_1/figures/"+str(nn[0])+"/total_lane_num_"+str(nn[0])+".png")
        plt.show()
        
        plt.plot(updates, avlane)
        plt.xlabel("Timesteps")
        plt.ylabel("Total Number of Lane Changes by AV")
        plt.title("Number of Lane Changes (AV) over time")
        plt.savefig("draft_2/experiment_1/figures/"+str(nn[0])+"/total_lane_av_"+str(nn[0])+".png")
        plt.show()
        
        plt.plot(updates, rvlane)
        plt.xlabel("Timesteps")
        plt.ylabel("Total Number of Lane Changes by RV")
        plt.title("Number of Lane Changes (RV) over time")
        plt.savefig("draft_2/experiment_1/figures/"+str(nn[0])+"/total_lane_rv_"+str(nn[0])+".png")
        plt.show()
        
        plt.plot(updates, carclus)
        plt.xlabel("Timesteps")
        plt.ylabel("Ratio")
        plt.title("Clusterability")
        plt.ylim(0,0.4)
        plt.savefig("draft_2/experiment_1/figures/"+str(nn[0])+"/tclusterability_"+str(nn[0])+".png")
        plt.show()
                
        plt.plot(updates, cum_clnum )
        plt.xlabel("Timesteps")
        plt.ylabel("Total Number of Clusters")
        plt.title("Number of Clusters over time")
        plt.savefig("draft_2/experiment_1/figures/"+str(nn[0])+"/total_cluster_num_"+str(nn[0])+".png")
        plt.show()
        
        plt.plot(updates, prob)
        plt.xlabel("Timesteps")
        plt.ylabel("Proportion of AV-AV headways")
        plt.title("Probability of AV-AV headways")
    #    plt.ylim(0,0.12)
        plt.savefig("draft_2/experiment_1/figures/"+str(nn[0])+"/prob_AV-AV_"+str(nn[0])+".png")
        plt.show()
        
        
        plt.plot(updates, clnum )
        plt.xlabel("Timesteps")
        plt.ylabel("Number of Clusters")
        plt.title("Number of Clusters over time")
        plt.savefig("draft_2/experiment_1/figures/"+str(nn[0])+"/cluster_num_"+str(nn[0])+".png")
        plt.show()
        
        plt.plot(updates, avgclsize)
        plt.xlabel("Timesteps")
        plt.ylabel("Average Size of Clusters")
    #    plt.ylim(0,16)
        plt.title("Average Size of Clusters over time")
        plt.savefig("draft_2/experiment_1/figures/"+str(nn[0])+"/cluster_size_"+str(nn[0])+".png")
        plt.show()
        
        """     
        plt.plot(time, clnum)
        plt.xlabel("time (s)")
        plt.ylabel("Number of Clusters")
        plt.title("Number of Clusters over time")
        plt.savefig("cluster_num_"+str(nn[0])+".png")
        plt.show()
        
        plt.plot(time, avgclsize)
        plt.xlabel("time (s)")
        plt.ylabel("Average Size of Clusters")
        plt.title("Average Size of Clusters over time")
        plt.savefig("cluster_size_"+str(nn[0])+".png")
        plt.show()
        """
        
        plt.scatter(densityrv, flowrv, s= 1)
        plt.xlabel("RV density")
        plt.ylabel("RV flow")
        plt.title("Fundamental Diagram: RV")  
        plt.savefig("draft_2/experiment_1/figures/"+str(nn[0])+"/fd-rv"+str(nn[0])+".png")
        plt.show()
        
        plt.scatter(densityav, flowav, s= 1)
        plt.xlabel("AV density")
        plt.ylabel("AV flow")
        plt.title("Fundamental Diagram: AV") 
        plt.savefig("draft_2/experiment_1/figures/"+str(nn[0])+"/fd-av"+str(nn[0])+".png")
        plt.show()
        
        
        plt.scatter(density, flow, s= 1)
        plt.xlabel("density")
        plt.ylabel("flow")
        plt.title("Fundamental Diagram")  
        plt.savefig("draft_2/experiment_1/figures/"+str(nn[0])+"/fd-data"+str(nn[0])+".png")
        plt.show()
        
        #still need to include code for different visualization
        
        # histo for size
        histo(avgclsize, "Mean cluster size", nn[0])
        
        # histo for cluster num
        histo(clnum, "Number of clusters", nn[0])
        
        # histo for time cluster stays 
        
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
    frequencies = freq # frequency of x axis values

#    print(alphab)
#    print(freq)
    
    sum_freq = 0
    sum_numer = 0
    
    for i in range(len(alphab)):
        sum_freq += freq[i]
        sum_numer += (alphab[i]*freq[i])
    
    if sum_freq == 0:
        w_mean = 0
    else:
        w_mean = ( sum_numer / sum_freq )
    
    pos = np.arange(len(alphab))
    
    file1 = open("draft_2/experiment_1/data_files/average_parameters_for_all_cases_combined.txt","a+") 
    file1.write("Average of " + str(q3) + " is "  + str(w_mean) + " for " + str(nn) + "\n")
    file1.close()
    
    width = 0.5     # gives histogram aspect to the bar diagram
    
    ax = plt.axes()
    ax.set_xticks(pos)
    ax.set_xticklabels(alphab)
    
    plt.bar(pos, frequencies, width)
    plt.xlabel(q3)
    plt.ylabel("frequency")
    plt.title("Histogram of " + str(q3))  
   # plt.ylim(0,22)
    plt.xticks(rotation=45)
    plt.savefig("draft_2/experiment_1/figures/"+str(nn)+"/hist"+str(q3)+str(nn)+".png")
    plt.show()
    
        
name1 = "draft_2/experiment_1/data_files/low_dens_oppo.txt"
name2 = "draft_2/experiment_1/data_files/low_dens_aware.txt"
name3 = "draft_2/experiment_1/data_files/low_dens_base.txt"

name4 = "draft_2/experiment_1/data_files/crit_dens_oppo.txt"
name5 = "draft_2/experiment_1/data_files/crit_dens_aware.txt"
name6 = "draft_2/experiment_1/data_files/crit_dens_base.txt"

name7 = "draft_2/experiment_1/data_files/high_dens_oppo.txt"
name8 = "draft_2/experiment_1/data_files/high_dens_aware.txt"
name9 = "draft_2/experiment_1/data_files/high_dens_base.txt"

namei = "draft_2/experiment_1/data_files/mid_dens_oppo.txt"
nameii = "draft_2/experiment_1/data_files/mid_dens_aware.txt"
nameiii = "draft_2/experiment_1/data_files/mid_dens_base.txt"

m1 = plot1(name8)
plot1(name9)
#plot1(nameiii)

"""
plot_all = [name1,name2,name3,name4,name5,name6,name7,name8,name9]

for i in plot_all:
    plot1(i)

"""

