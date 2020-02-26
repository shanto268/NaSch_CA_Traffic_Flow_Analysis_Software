#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 00:10:06 2020

@author: sshanto
"""

import numpy as np
import matplotlib.pyplot as plt

def ana():
    f = open("draft_2/experiment_1/data_files/average_parameters_for_all_cases_combined.txt","r") 
    titles = []
    vals = []
    cases = []
    time = []
    time_t = []
    clsize = []
    clnum = []
    clsize_t = []
    clnum_t = []
    
    for x in f:
        x = x.split(" ")
        y = x[2:5]
        title = "_".join(y)
        val = float(x[-3])
        case = x[-1]
        case = [i for i in case if i != "\n"]
        case = "".join(case)
        if title == "Time_period_of":
            if val != 1199.0 :
                time.append(val)
                time_t.append(case)
        
        if title == "Mean_cluster_size":
                clsize.append(val)
                clsize_t.append(case)
                
        if title == "Number_of_clusters":
                clnum.append(val)
                clnum_t.append(case)
        
        titles.append(title)
        vals.append(val)
        cases.append(case)

    return titles, vals, cases, time, time_t, clsize, clnum, clsize_t, clnum_t
    
sim_type = ana()[2]
param = ana()[0]
param_val = ana()[1]
time = ana()[3]
group = ana()[4]

grp = ana()[7]
clsize = ana()[5]
clnum =ana()[6]

def shrt(q):
    x = []
    for i in q:
        x.append(i[0])
    res = "".join(x)
    return res

def plotter(fig, t, group,key):
    types = []
    for i in group:
        types.append(shrt(i.split("_")))
    x_coords = [i for i in range(len(t))]
    y_coords = t
    
    print(types)
    
    for i,type in enumerate(types):
        x = x_coords[i]
        y = y_coords[i]
        plt.scatter(x, y, marker='x')
        plt.text(x-0.5, y+0.006, type, fontsize=9)
    plt.title("Average Survival "+key+ " for different Models and Regimes")
    plt.ylabel("Average Survival " +key)
    plt.savefig("draft_2/experiment_1/figures/" + fig)
    plt.show()
"""
plotter("time_report_exp1.png", time, group, "Time")
plotter("cluster_size_report_exp1.png", clsize, grp, "Cluster Size")
plotter("cluster_num_report_exp1.png", clnum, grp, "Cluster Number")
"""

def ana_clusterability():
    f = open("draft_2/experiment_1/data_files/clusterability.txt","r") 
    titles = []
    clval = []
    for x in f:
        x = x.split(",")
        titles.append(x[0])
        y = float((x[1].split("\n")[0]))
        clval.append(y)
    return titles, clval

tit = ana_clusterability()[0]
c1 = ana_clusterability()[1]

print(tit)

plotter("clusterability_report.png", c1, tit, "Clusterability")







# plot and think about comparing other values for analysis


    