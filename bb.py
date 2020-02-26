#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:36:47 2020

@author: sshanto
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

f = [8.2, 7.4, 6.8, 5.5, 5.2]
V2 = [1.901, 1.578, 1.422, 0.856, 0.723]
V4 = [1.497, 0.802, 0.745, 0.731, 0.729]
V8 = [1.962, 1.697, 1.493, 0.940, 0.771]

plt.scatter(f, V2)
plt.plot(np.unique(f), np.poly1d(np.polyfit(f, V2, 1))(np.unique(f)))
plt.scatter(f, V4)
plt.plot(np.unique(f), np.poly1d(np.polyfit(f, V4, 1))(np.unique(f)))
plt.scatter(f, V8)
plt.plot(np.unique(f), np.poly1d(np.polyfit(f, V8, 1))(np.unique(f)))
plt.plasma()
plt.show()

