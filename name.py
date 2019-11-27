# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:38:44 2019

@author: Owner
"""

def name(x):
    y = x.split('/')
    t = y[2].split('\\')
    tf = t[0] + "/" + t[1] + "/" + "combined_" + t[1] + ".pdf"
    ti = y[0] + "/" + y[1] + "/" + tf
    return ti

i = name('draft_2/experiment_1/figures\\low_dens_oppo\\cluster_num_low_dens_oppo.png')
#print(i)


drt = "draft_2/experiment_1/figures/low_dens_oppo/"
print(drt.split("/"))