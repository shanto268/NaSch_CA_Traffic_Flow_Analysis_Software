import numpy as np
import collections

#avs_x = [12, 17, 18, 21, 23 , 26, 34, 54, 57, 60, 63, 99]

#avs_x = [0, 2, 5, 12, 17, 18, 21, 23 , 26, 34, 54, 57, 60, 63, 99]

avs_x = [0, 3, 3, 6, 9, 12, 17, 18, 21, 23 , 26, 34, 54, 57, 60, 63, 91, 95, 97]
update = 1
#provision for clustering in loop boundaries
print("\nInput " + str(avs_x) +"\n")
gap = 3
cluster_thresh = 4
count = 0
cluster_num_car = 0 #new add 2020 SAS
clustersize = []
loop = []

MC = []
MC.append([])
u = 0
for i in range(len(avs_x)):
    j=i+1
    if j < len(avs_x) and (avs_x[j] - avs_x[i]) <= gap:
        MC[u].append(avs_x[i])  
        if j == (len(avs_x) - 1):
            MC[u].append(avs_x[j])
        elif (j < len(avs_x)) and (avs_x[j+1] - avs_x[j]) > gap:
            MC[u].append(avs_x[j])  
            MC.append([])
            u += 1 
    if avs_x[i] >= 90 or avs_x[i] <= 10:
        loop.append(avs_x[i])

        #create a new array with x positions of cars > 90 and < 10
'''
for arr in range(len(MC)):
    print(arr)
'''
#print("Mega cluster old: " + str(MC))

for i in range(len(MC)):
    if i == (len(MC) - 1):
        for j in range(len(MC[i])):
            if j == (len(MC[i])-1):
                last = MC[i][j]

first = MC[0][0]

if (first + 100) - last <= gap:
    join = MC[0] + MC[len(MC)-1]
    MC.pop()
    MC.pop(0)
    MC.append(join)

MC.sort()
    
print("Mega cluster new: " + str(MC)+"\n")


#print(join)


for arr in MC:
    if len(arr) >= cluster_thresh:
        clustersize.append(len(arr))
        cluster_num_car += len(arr)
        count += 1
        
print("cluster size: " + str(clustersize)) # get average
print("numbers of cars in cluster: " + str(cluster_num_car))
clinfo = []

avg_size = 0
for size in clustersize:
    avg_size += size 
    clinfo.append((size,update))

off_size = avg_size / count
print("number of cluster " + str(count)) #distribute this count over time

print("avg cluster size: " + str(off_size)) #distribute this over time

print("clinfo: " + str(clinfo))

#print("\nBOUNDARY: "+str(loop))


                                                       #new code:


#new = [(4, 5), (4, 6), (4,7), (4, 32), (4, 41), (4, 43), (6,48) ,(4, 54), (4, 55), (4, 56), (4, 57), (4, 58), (4, 59), (5,60), (5,61)]
new = [(5, 0), (4, 2), (4, 6), (5, 10), (4, 10), (4, 10), (5, 11), (4, 11), (4, 11), (5, 12), (4, 12), (5, 13), (4, 13), (4, 13), (5, 14)]

new = sorted(new , key= lambda k: [k[0], k[1]])

#print(new)
#print('')
clstr = []

for i in range(len(new)):
    j=i+1
    if j < len(new) and (new[i][0] == new[j][0] and (new[j][1] - new[i][1]) == 1):
        clstr.append(new[j])
        
#print(clstr)

final = [item for item in new if item not in clstr]       
size = []
time = []

#final = sorted(final , key= lambda k: [k[0], k[1]])

for ele in final:
    size.append(ele[0])

'''
for i in range(len(final)):
    j=i+1
    if j < len(final) and ((final[j][1] - final[i][1] == 0) or (final[j][1] - final[i][1] == 1)) :
        print(final[i])
'''

'''
new algorithm:
    detect copies
    sort in time for each copy
    take out longest chain
'''
solution = [(4, 2), (4, 6), (4, 10), (4, 10), (4, 13), (5, 0), (5, 10)]
#take out the longest chain keeping first head



print('')
#print(final)
#print('') 
#print(len(final))                
print('')
#print(solution)
#print(time)
