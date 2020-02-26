#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:40:30 2020

@author: sshanto
"""

import numpy as np
import matplotlib.pyplot as plt
 
# Make a fake dataset:
height = [23.419354838709676, 12.745454545454546, 4.7, 5.7384615384615385, 2.4285714285714284]
bars = ('oppo and aware', 'oppo', 'aware', 'base 2', 'base 1')
y_pos = np.arange(len(bars))
 
plt.bar(y_pos, height)
plt.xticks(y_pos, bars)
plt.title("Low Density: Average Survival Time")
plt.ylim(0,26)
plt.show()


height = [34.6875, 25.523809523809526, 14.772727272727273, 11.1, 6.666666666666667]
bars = ('oppo and aware', 'oppo', 'aware', 'base 2', 'base 1')
y_pos = np.arange(len(bars))
 
plt.bar(y_pos, height)
plt.xticks(y_pos, bars)
plt.title("Critical Density: Average Survival Time")
plt.show()

