# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:10:50 2019

@author: Owner
"""
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

header_info = "density, flow,updates, densityrv, flowrv, densityav, flowav, cluster, avgclus, freq\n"
file_name = "info.txt"

def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
 #   os.rename('newfile.txt',originalfile)
    return 'newfile.txt'

nout = insert(file_name, header_info)


data = pd.read_csv(nout, skipinitialspace=True)
data['cluster'].hist(bins=5, grid=False, xlabelsize=11, ylabelsize=11)
plt.xlabel("Cluster Number", fontsize=13)
plt.ylabel("Frequency",fontsize=13)
plt.xlim([0.0,10.0])
plt.show()

data = pd.read_csv(nout, skipinitialspace=True)
data['avgclus'].hist(bins=10, grid=False, xlabelsize=11, ylabelsize=11)
plt.xlabel("Cluster Size", fontsize=13)
plt.ylabel("Frequency",fontsize=13)
plt.xlim([0.0,20.0])


#sns.distplot(data['cluster'])

"""
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(low=0, high=100, size=100)

print(x)

# Compute frequency and bins
frequency, bins = np.histogram(x, bins=100, range=[0, 100])
plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})
plt.hist(x, bins)
plt.gca().set(title='Frequency Histogram', ylabel='Frequency');

"""
    
plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

# Plot Histogram on x
x = np.random.normal(size = 1000)
plt.hist(x, bins=50)
plt.gca().set(title='Frequency Histogram', ylabel='Frequency');

    
    
"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    