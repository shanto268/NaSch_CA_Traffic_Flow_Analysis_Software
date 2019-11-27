# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:43:49 2019

@author: Owner
"""
import random
import numpy as np
mu, sigma = .15, .05                        # mean and standard deviation 
avprob = np.random.normal(mu, sigma, 100) 
x =random.randint(0,99)
prob_av = avprob[x]
print("Prob(AV): " + str(prob_av * 100))
prob_rv = 1 - prob_av
print("Prob(RV): " + str(prob_rv * 100))
y = random.uniform(0, 1)
z = random.uniform(0.38,0.4)
d_av = abs(y - prob_av + z)
d_rv = abs(y - prob_rv)
print("d(AV): " + str(d_av))
print("d(RV): " + str(d_rv))
w = min(d_rv,d_av)  
if w == d_rv:
    print("Choice: RV " + str(w))
else:
    print("Choice: AV " + str(w))
print("")
if w == d_rv: #case: RV
    vtype = 1
    #return vtype
elif w == d_av :         #case: AV                                
    vtype = 2
'''
mu, sigma = .30, .05                        # mean and standard deviation 
        avprob = np.random.normal(mu, sigma, 100) 
        x =random.randint(0,99)
        prob_av = avprob[x]
     #   print("Prob(AV): " + str(prob_av))
        prob_rv = 1 - prob_av
   #     print("Prob(RV): " + str(prob_rv))
        y = random.uniform(0, 1)
        z = random.uniform(0.38,0.4)
        d_av = abs(y - prob_av + z)
        d_rv = abs(y - prob_rv)
        print("d(AV): " + str(d_av))
        print("d(RV): " + str(d_rv))
        w = min(d_rv,d_av)  
      #  print("Choice: " + str(w))
       # print("")
        if w == d_rv: #case: RV
          vtype = 1
          return vtype
        elif w == d_av :         #case: AV                                
         vtype = 2
         return vtype
'''