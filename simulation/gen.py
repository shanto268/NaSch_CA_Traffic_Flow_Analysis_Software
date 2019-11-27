# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:23:36 2019

@author: Owner
"""
import random
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = .3, .05 # mean and standard deviation
avprob = np.random.normal(mu, sigma, 100) 
print(avprob)
x =random.randint(0,99)
prob_av = avprob[x]       

plt.hist(avprob, 50,
         density=True,
         histtype='bar',
         facecolor='o',
         alpha=0.5)

plt.show()

print("Prob(AV): " + str(prob_av))
prob_rv = 1 - prob_av
#print("Prob(RV): " + str(prob_rv))
y = random.uniform(0, 1)
z = random.uniform(0.15, 0.22)
d_av = abs(y - prob_av + z)
d_rv = abs(y - prob_rv)
#print("d(AV): " + str(d_av))
#print("d(RV): " + str(d_rv))
w = min(d_rv,d_av)  
      #  print("Choice: " + str(w))
       # print("")