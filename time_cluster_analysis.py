# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:09:04 2019

@author: Owner


import sys


fn = sys.argv[1]
new_nn = fn.split('/')
fn = new_nn[3]
nn = fn.split('.')
print(nn[0])


import numpy as np
import matplotlib.pyplot as plt

alphab = [1,2,3,4,5,6]
frequencies = [23, 44, 12, 11, 2, 10]

pos = np.arange(len(alphab))
width = 0.5     # gives histogram aspect to the bar diagram

ax = plt.axes()
ax.set_xticks(pos)
ax.set_xticklabels(alphab)

plt.bar(pos, frequencies, width, color='b')
plt.show()

"""

"""
a = [4,4,4,4,4,4,2,2,2,2,3,2,12,213,12,12,5,2,2,2,1,5,5,5,5,2,2,12]

b = [[x,a.count(x)] for x in set(a)]
num = []
freq = []
for i in b:
#    print("num : " + str(i[0]))
    num.append(i[0])
#    print("and freq: "+str(i[1]))
    freq.append(i[1])

print(num)
print(freq)


"""
# = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
a = [0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 5, 5, 7, 6, 5, 5, 0, 4, 4, 5, 5, 0, 1,2,2,0,1,1]
#time = [3,5,]

time = []
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
                time.append(t)
        else:
            time.append(t)
            t = 0
#print(index)
print(time)

"""
for i in range(len(time)):
    time[i] = time[i] + 1
    
print(time)
"""
