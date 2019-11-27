from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import csv
import scipy, matplotlib
from scipy.optimize import curve_fit
from scipy.optimize import differential_evolution
import warnings



def plot1(fname):
        fn = fname
        nn = fn.split('b.')        
        fr = 'dummy' + str(fname) + '.txt'
        #dnewdata = "0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "
        dnewdata = "dnew line"
        with open(fn, 'r') as f:
            lines = f.read().split('\n')
            #to delete line use "del lines[4]"
            #to replace line:
            for i in range(0,len(lines)):    
                if (i % 100)  == 0 or (i % 100) < 19 and i > 0:  #or (i % 4)  == 1 :
                    lines[i] = dnewdata
        with open(fr,'w') as f:
            f.write('\n'.join(lines))
        
        with open(fr, "r") as f:
            lines = f.readlines()
        with open(fr, "w") as f:
            for line in lines:
                if line.strip("\n") != "dnew line":
                    f.write(line)
                    
        with open(fr, "r+") as f:     #fr change
            a = f.read()
        
        with open(fr, "w+") as f:     #fr change
                f.write("0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  \n" + a)
        
        
        density = []
        flow = []
        updates = []
        densityrv = []
        flowrv = []
        densityav = []
        flowav = []        
        clnum = []
        avgclsize = []
#        clsize = [] 
        
        with open(fr,'r') as csvfile:
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
 #               clsize.append(float(row[11]))
            
        FD_arr = []
        params = []  #fd, fdrv, fdav
        FD_RV_arr = []
        FD_AV_arr = []
        
        
        plt.plot(updates, clnum)
        plt.xlabel("Timesteps")
        plt.ylabel("Number of Clusters")
        plt.title("Number of Clusters over time")
        plt.savefig("final/new/cluster_num_"+str(nn[0])+".pdf")
        plt.show()
        
        plt.plot(updates, avgclsize)
        plt.xlabel("Timesteps")
        plt.ylabel("Average Size of Clusters")
        plt.title("Average Size of Clusters over time")
        plt.savefig("final/new/cluster_size_"+str(nn[0])+".pdf")
        plt.show()
        
        
        plt.scatter(flowrv, flow, s= 1)
        plt.xlabel("RV flow")
        plt.ylabel("Overall flow")
        plt.title("Overall flow vs RV flow")  
        plt.savefig("final/new/flowrv"+str(nn[0])+".pdf")
        plt.show()
        
        plt.scatter(flowav, flow, s= 1)
        plt.xlabel("AV flow")
        plt.ylabel("Overall flow")
        plt.title("Overall flow vs AV flow")  
        plt.savefig("final/new//flowav"+str(nn[0])+".pdf")
        plt.show()
        
        plt.scatter(densityrv, flowrv, s= 1)
        plt.xlabel("RV density")
        plt.ylabel("RV flow")
        plt.title("Fundamental Diagram: RV")  
        plt.savefig("final/new//fdrv"+str(nn[0])+".pdf")
        plt.show()
        
        plt.scatter(densityav, flowav, s= 1)
        plt.xlabel("AV density")
        plt.ylabel("AV flow")
        plt.title("Fundamental Diagram: AV") 
        plt.savefig("final/new//flowav"+str(nn[0])+".pdf")
        plt.show()
        
        
        plt.scatter(density, flow, s= 1)
        plt.xlabel("density")
        plt.ylabel("flow")
        plt.title("Fundamental Diagram")  
        plt.savefig("final/new//fddata"+str(nn[0])+".pdf")
        plt.show()
        
        flow_max_index = flow.index(max(flow))
        flowrv_max_index = flowrv.index(max(flowrv))
        flowav_max_index = flowav.index(max(flowav))
        
        x = density
        y =flow
        N= 3000
        
        def piecewise_linear(x, x0, y0, k1, k2):
            return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])
        
        p0 = [np.mean(x), np.mean(y), 1, 1]
                    #weighing functions:            
                    
        y_weight = np.empty(len(y))
        y_weight.fill(10)
        y_weight[0] = y_weight[-5:-1] = 0.1
        y_weight[flow_max_index] = 0.2
        
        
        p , e = optimize.curve_fit(piecewise_linear, x, y, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
        perr = np.sqrt(np.diag(e))
        xd = np.linspace(0, 1, N)
        
        x0, y0, k1, k2 = p
                                                                                #function and coefficients
        y_crit = y0 #max flow
        x_crit = x0 #critical density
        x_jam = max(xd) #jam density
        def x_intercept(slope, yi, xi):
            return (slope*xi - yi)/ slope
        x_jam = min(x_intercept(k2, y0, x0),1)                                  #NEED TO RETURN THIS
        free_y = k1   #slope 1
        wave_v = k2    #slope 2
        

        plt.plot(xd, piecewise_linear(xd, *p), 'orange', label = 'fit')             #NEED TO RETURN THIS
        plt.scatter(x,y,color = 'mediumblue', s=3, marker = ".", label = 'data')
        plt.legend()
        plt.xlabel('density')
        plt.ylabel('flow')
        plt.title('Fundamental diagram: ')
        plt.savefig("final/new//fdfit"+str(nn[0])+".pdf")
        plt.show()
        
        #print("[x_critical  y_max  free_flow_v  wave_speed]")
        #print(p)                                                                                    #NEED TO RETURN THIS
        #print("jam density: " + str(x_jam))        
        
        plt.plot(xd, piecewise_linear(xd, *p), 'orange')   
        plt.xlabel('density')
        plt.ylabel('flow')
        plt.title('Fundamental diagram: ')
        plt.savefig("final/new//fdtri"+str(nn[0])+".pdf")
        plt.show()
        
        FD_arr.append(xd)
        FD_arr.append( piecewise_linear(xd, *p)) 
        
        """
        plt.plot(lan, updates)
        plt.xlabel('time steps')
        plt.ylabel('Number of lane changes to test lane')
        plt.savefig("final/new//lane"+str(nn[0])+".pdf")
        plt.show()
        """
        
        xrv = densityrv
        yrv= flowrv        
        
        y_weight = np.empty(len(yrv))
        y_weight.fill(10)
        y_weight[0] = y_weight[-5:-1] = 0.1
        y_weight[flowrv_max_index] = 0.2
        
        p0 = [np.mean(xrv), np.mean(yrv), 1, 1]
        prv , e = optimize.curve_fit(piecewise_linear, xrv, yrv, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
        perr = np.sqrt(np.diag(e))
        #xdrv = np.linspace(0, max(xrv), 3000)
        xdrv = np.linspace(0, 1, 3000)
        
        plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'orange')     #need to return this
        plt.xlabel('RV density')
        plt.ylabel('RV flow')
        plt.gca().set_xlim([0,max(densityrv)+0.05])
        plt.gca().set_ylim([0, max(flowrv) + 0.05])
        plt.title('RV Fundamental diagram: ')
        plt.savefig("final/new//trirv"+str(nn[0])+".pdf")
        plt.show()
        
        FD_RV_arr.append(xdrv)
        FD_RV_arr.append( piecewise_linear(xdrv, *prv))

        xav = densityav
        yav= flowav        
        
        y_weight = np.empty(len(yav))
        y_weight.fill(10)
       # y_weight[0] = y_weight[-5:-1] = 0.1 #works for model 1
        y_weight[0] =  0.1
      #  y_weight[int(len(yav) - 1)] = 0.1  #worked for r1m1
        y_weight[0] = y_weight[-5:-1] = 0.01
        y_weight[flowav_max_index] = 0.01
        
        p0 = [np.mean(xav), np.mean(yav), 1, 1] 
        pav , e = optimize.curve_fit(piecewise_linear, xav, yav, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
        perr = np.sqrt(np.diag(e))
        #xdav = np.linspace(0, max(xav), 3000)
        xdav = np.linspace(0, 1, 3000)
        
        plt.plot(xdav, piecewise_linear(xdav, *pav), 'orange')     #need to return this
        plt.xlabel('AV density')
        plt.ylabel('AV flow')
        plt.gca().set_xlim([0,max(densityav)+0.05])
        plt.gca().set_ylim([0, max(flowav) + 0.05])
        plt.title('AV Fundamental diagram: ')
        plt.savefig("final/new//triav"+str(nn[0])+".pdf")
        plt.show()
    
        FD_AV_arr.append(xdav)
        FD_AV_arr.append( piecewise_linear(xdav, *pav))
        
        params.append(p)
        params.append(prv)
        params.append(pav)
        
        plt.plot(xdav, piecewise_linear(xdav, *pav), 'orange', label='AV')  
        plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'green', label='RV')  
        plt.plot(xd, piecewise_linear(xd, *p), 'blue', label='Overall')  
        plt.ylim(0, 0.7)
        plt.xlim(0,1)
        plt.legend()
        plt.title('Fundamental diagram: ')
        plt.savefig("final/new//triall"+str(nn[0])+".pdf")
        plt.show()
        
        
        return FD_arr, FD_RV_arr, FD_AV_arr, params
         
        
        
        
        
    
r1m1 = plot1('type_aware_crit_density.txt')
#r1m2 = plot1('type_unaware_crit_density.txt')
#r2m1 = plot1('control_crit_density.txt')


#print(r1m1[5])
#print(r1m2[5])
#print(r2m1[5])

"""

def plot2(arr1, arr2, arr3):
    d1 = arr1[0][0]
    d2 = arr2[0][0]
    d3 = arr3[0][0]
    
    q1 = arr1[0][1] 
    q2 = arr2[0][1] 
    q3 = arr3[0][1] 
    
    drv1 = arr1[1][0]
    drv2 = arr2[1][0] 
    drv3 = arr3[1][0]
    
    qrv1 = arr1[1][1]
    qrv2 = arr2[1][1] 
    qrv3 = arr3[1][1]
    
    
    dav1 = arr1[2][0] 
    dav2 = arr2[2][0]  
    dav3 = arr3[2][0]  
    
    qav1 = arr1[2][1]
    qav2 = arr2[2][1]
    qav3 = arr3[2][1]
    
    
    
    l1 = np.diff(arr1[4])
    l2 = np.diff(arr2[4])
    l3 = np.diff(arr3[4])
    
    plt.plot(d1, q1, 'r:' ,label = "aware")
    plt.plot( d2, q2, 'y' ,label = "unaware")
    plt.plot(d3, q3, 'b:' ,label = "control")
    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Fundamental diagram: ')
    plt.savefig("final/"+"/tricomp.pdf")
    plt.show()
    
    #plt.plot(drv1, qrv1, label = "aware", drv2, qrv2, label = "aware",drv3, qrv3, label = "control",drv4, qrv4, label = "R2M2")
    plt.plot(drv1, qrv1, 'r:' ,label = "aware")
    plt.plot( drv2, qrv2, 'y' ,label = "unaware")
    plt.plot(drv3, qrv3, 'b:' ,label = "control")
    plt.ylim(0, 0.7)
    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Fundamental diagram: RV')
    plt.savefig("final/"+"/tricomprv.pdf")
    plt.show()
    
  #  plt.plot(dav1, qav1, label = "aware", dav2, qav2, label = "unaware",dav3, qav3, label = "control",dav4, qav4, label = "R2M2")
    plt.plot(dav1, qav1, 'r:' ,label = "aware")
    plt.plot( dav2, qav2, 'y' ,label = "unaware")
    plt.plot(dav3, qav3, 'b:' ,label = "control")
    plt.ylim(0, 0.7)
    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Fundamental diagram: AV')
    plt.savefig("final/"+"/tricompav.pdf")    
    plt.show()
    
    plt.plot(range(len(l1)), l1  ,label = "aware") 
    plt.plot(range(len(l2)), l2  ,label = "unaware")
    plt.plot(range(len(l3)), l3 ,label = "control")
    plt.xlabel('time steps')
    plt.legend()
    plt.ylabel('Number of lane changes to test lane')
    plt.savefig("final/"+"/lanecomprv.pdf")    
    plt.show()
    
    
    
    
    
plot2(r1m1, r1m2, r2m1)    


"""









































"""

def plot1(fname):
        fn = fname
        nn = fn.split('b.')        
        fr = 'dummy' + str(fname) + '.txt'
        #dnewdata = "0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "
        dnewdata = "dnew line"
        with open(fn, 'r') as f:
            lines = f.read().split('\n')
            #to delete line use "del lines[4]"
            #to replace line:
            for i in range(0,len(lines)):    
                if (i % 100)  == 0 or (i % 100) < 19 and i > 0:  #or (i % 4)  == 1 :
                    lines[i] = dnewdata
        with open(fr,'w') as f:
            f.write('\n'.join(lines))
        
        with open(fr, "r") as f:
            lines = f.readlines()
        with open(fr, "w") as f:
            for line in lines:
                if line.strip("\n") != "dnew line":
                    f.write(line)
                    
        with open(fr, "r+") as f:     #fr change
            a = f.read()
        
        with open(fr, "w+") as f:     #fr change
                f.write("0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  \n" + a)
        
        
        density = []
        flow = []
        updates = []
        densityrv = []
        flowrv = []
        densityav = []
        flowav = []        
        lan = []
        freq = []
        
        with open(fr,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                density.append(float(row[0]))
                flow.append(float(row[1]))
                updates.append(float(row[2]))
                densityrv.append(float(row[3]))
                flowrv.append(float(row[4]))
                densityav.append(float(row[5]))
                flowav.append(float(row[6]))
                lan.append(float(row[7]))
                freq.append(float(row[8]))
        
        FD_arr = []
        params = []  #fd, fdrv, fdav
        FD_RV_arr = []
        FD_AV_arr = []
        L0_p = max(lan)
        pavav = (sum(freq) / len(freq))
        
        
        plt.scatter(flowrv, flow, s= 1)
        plt.xlabel("RV flow")
        plt.ylabel("Overall flow")
        plt.title("Overall flow vs RV flow")  
        plt.savefig("final/"+str(nn[0])+"/flowrv"+str(nn[0])+".pdf")
        plt.show()
        
        
        
        plt.scatter(flowav, flow, s= 1)
        plt.xlabel("AV flow")
        plt.ylabel("Overall flow")
        plt.title("Overall flow vs AV flow")  
        plt.savefig("final/"+str(nn[0])+"/flowav"+str(nn[0])+".pdf")
        plt.show()
        
        plt.scatter(densityrv, flowrv, s= 1)
        plt.xlabel("RV density")
        plt.ylabel("RV flow")
        plt.title("Fundamental Diagram: RV")  
        plt.savefig("final/"+str(nn[0])+"/fdrv"+str(nn[0])+".pdf")
        plt.show()
        
        plt.scatter(densityav, flowav, s= 1)
        plt.xlabel("AV density")
        plt.ylabel("AV flow")
        plt.title("Fundamental Diagram: AV") 
        plt.savefig("final/"+str(nn[0])+"/flowav"+str(nn[0])+".pdf")
        plt.show()
        
        
        plt.scatter(density, flow, s= 1)
        plt.xlabel("density")
        plt.ylabel("flow")
        plt.title("Fundamental Diagram")  
        plt.savefig("final/"+str(nn[0])+"/fddata"+str(nn[0])+".pdf")
        plt.show()
        
        flow_max_index = flow.index(max(flow))
        flowrv_max_index = flowrv.index(max(flowrv))
        flowav_max_index = flowav.index(max(flowav))
        
        x = density
        y =flow
        N= 3000
        
        def piecewise_linear(x, x0, y0, k1, k2):
            return np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])
        
        p0 = [np.mean(x), np.mean(y), 1, 1]
                    #weighing functions:            
                    
        y_weight = np.empty(len(y))
        y_weight.fill(10)
        y_weight[0] = y_weight[-5:-1] = 0.1
        y_weight[flow_max_index] = 0.2
        
        
        p , e = optimize.curve_fit(piecewise_linear, x, y, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
        perr = np.sqrt(np.diag(e))
        xd = np.linspace(0, 1, N)
        
        x0, y0, k1, k2 = p
                                                                                #function and coefficients
        y_crit = y0 #max flow
        x_crit = x0 #critical density
        x_jam = max(xd) #jam density
        def x_intercept(slope, yi, xi):
            return (slope*xi - yi)/ slope
        x_jam = min(x_intercept(k2, y0, x0),1)                                  #NEED TO RETURN THIS
        free_y = k1   #slope 1
        wave_v = k2    #slope 2
        

        plt.plot(xd, piecewise_linear(xd, *p), 'orange', label = 'fit')             #NEED TO RETURN THIS
        plt.scatter(x,y,color = 'mediumblue', s=3, marker = ".", label = 'data')
        plt.legend()
        plt.xlabel('density')
        plt.ylabel('flow')
        plt.title('Fundamental diagram: ')
        plt.savefig("final/"+str(nn[0])+"/fdfit"+str(nn[0])+".pdf")
        plt.show()
        
        #print("[x_critical  y_max  free_flow_v  wave_speed]")
        #print(p)                                                                                    #NEED TO RETURN THIS
        #print("jam density: " + str(x_jam))        
        
        plt.plot(xd, piecewise_linear(xd, *p), 'orange')   
        plt.xlabel('density')
        plt.ylabel('flow')
        plt.title('Fundamental diagram: ')
        plt.savefig("final/"+str(nn[0])+"/fdtri"+str(nn[0])+".pdf")
        plt.show()
        
        FD_arr.append(xd)
        FD_arr.append( piecewise_linear(xd, *p)) 
        
        plt.plot(lan, updates)
        plt.xlabel('time steps')
        plt.ylabel('Number of lane changes to test lane')
        plt.savefig("final/"+str(nn[0])+"/lane"+str(nn[0])+".pdf")
        plt.show()
        
        
        xrv = densityrv
        yrv= flowrv        
        
        y_weight = np.empty(len(yrv))
        y_weight.fill(10)
        y_weight[0] = y_weight[-5:-1] = 0.1
        y_weight[flowrv_max_index] = 0.2
        
        p0 = [np.mean(xrv), np.mean(yrv), 1, 1]
        prv , e = optimize.curve_fit(piecewise_linear, xrv, yrv, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
        perr = np.sqrt(np.diag(e))
        #xdrv = np.linspace(0, max(xrv), 3000)
        xdrv = np.linspace(0, 1, 3000)
        
        plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'orange')     #need to return this
        plt.xlabel('RV density')
        plt.ylabel('RV flow')
        plt.gca().set_xlim([0,max(densityrv)+0.05])
        plt.gca().set_ylim([0, max(flowrv) + 0.05])
        plt.title('RV Fundamental diagram: ')
        plt.savefig("final/"+str(nn[0])+"/trirv"+str(nn[0])+".pdf")
        plt.show()
        
        FD_RV_arr.append(xdrv)
        FD_RV_arr.append( piecewise_linear(xdrv, *prv))

        xav = densityav
        yav= flowav        
        
        y_weight = np.empty(len(yav))
        y_weight.fill(10)
       # y_weight[0] = y_weight[-5:-1] = 0.1 #works for model 1
        y_weight[0] =  0.1
      #  y_weight[int(len(yav) - 1)] = 0.1  #worked for r1m1
        y_weight[0] = y_weight[-5:-1] = 0.01
        y_weight[flowav_max_index] = 0.01
        
        p0 = [np.mean(xav), np.mean(yav), 1, 1] 
        pav , e = optimize.curve_fit(piecewise_linear, xav, yav, p0, sigma = y_weight, absolute_sigma = True)  # set initial parameter estimates
        perr = np.sqrt(np.diag(e))
        #xdav = np.linspace(0, max(xav), 3000)
        xdav = np.linspace(0, 1, 3000)
        
        plt.plot(xdav, piecewise_linear(xdav, *pav), 'orange')     #need to return this
        plt.xlabel('AV density')
        plt.ylabel('AV flow')
        plt.gca().set_xlim([0,max(densityav)+0.05])
        plt.gca().set_ylim([0, max(flowav) + 0.05])
        plt.title('AV Fundamental diagram: ')
        plt.savefig("final/"+str(nn[0])+"/triav"+str(nn[0])+".pdf")
        plt.show()
    
        FD_AV_arr.append(xdav)
        FD_AV_arr.append( piecewise_linear(xdav, *pav))
        
        params.append(p)
        params.append(prv)
        params.append(pav)
        
        plt.plot(xdav, piecewise_linear(xdav, *pav), 'orange', label='AV')  
        plt.plot(xdrv, piecewise_linear(xdrv, *prv), 'green', label='RV')  
        plt.plot(xd, piecewise_linear(xd, *p), 'blue', label='Overall')  
        plt.ylim(0, 0.7)
        plt.xlim(0,1)
        plt.legend()
        plt.title('Fundamental diagram: ')
        plt.savefig("final/"+str(nn[0])+"/triall"+str(nn[0])+".pdf")
        plt.show()
        
        return FD_arr, FD_RV_arr, FD_AV_arr, params, lan, pavav
         
        
        
        
        
    
r1m1 = plot1('r1m1b.txt')
r1m2 = plot1('r1m2b.txt')
r2m1 = plot1('r2m1b.txt')
r2m2 = plot1('r2m2b.txt')

print(r1m1[5])
print(r1m2[5])
print(r2m1[5])
print(r2m2[5])


def plot2(arr1, arr2, arr3, arr4):
    d1 = arr1[0][0]
    d2 = arr2[0][0]
    d3 = arr3[0][0]
    d4 = arr4[0][0]
    
    q1 = arr1[0][1] 
    q2 = arr2[0][1] 
    q3 = arr3[0][1] 
    q4 = arr4[0][1] 
    
    drv1 = arr1[1][0]
    drv2 = arr2[1][0] 
    drv3 = arr3[1][0]
    drv4 = arr4[1][0]
    
    qrv1 = arr1[1][1]
    qrv2 = arr2[1][1] 
    qrv3 = arr3[1][1]
    qrv4 = arr4[1][1]
    
    
    dav1 = arr1[2][0] 
    dav2 = arr2[2][0]  
    dav3 = arr3[2][0]  
    dav4 = arr4[2][0] 
    
    qav1 = arr1[2][1]
    qav2 = arr2[2][1]
    qav3 = arr3[2][1]
    qav4 = arr4[2][1]
    
    
    
    l1 = np.diff(arr1[4])
    l2 = np.diff(arr2[4])
    l3 = np.diff(arr3[4])
    l4 = np.diff(arr4[4])
    '''
    plt.plot(d1, q1, 'r:' ,label = "R1M1")
    plt.plot( d2, q2, 'y' ,label = "R1M2")
    plt.plot(d3, q3, 'b:' ,label = "R2M1")
    plt.plot(d4, q4, 'g--',label = "R2M2")
    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Fundamental diagram: ')
    plt.savefig("final/"+"/tricomp.pdf")
    plt.show()
    
    #plt.plot(drv1, qrv1, label = "R1M1", drv2, qrv2, label = "R1M2",drv3, qrv3, label = "R2M1",drv4, qrv4, label = "R2M2")
    plt.plot(drv1, qrv1, 'r:' ,label = "R1M1")
    plt.plot( drv2, qrv2, 'y' ,label = "R1M2")
    plt.plot(drv3, qrv3, 'b:' ,label = "R2M1")
    plt.plot(drv4, qrv4, 'g--',label = "R2M2")
    plt.ylim(0, 0.7)
    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Fundamental diagram: RV')
    plt.savefig("final/"+"/tricomprv.pdf")
    plt.show()
    
  #  plt.plot(dav1, qav1, label = "R1M1", dav2, qav2, label = "R1M2",dav3, qav3, label = "R2M1",dav4, qav4, label = "R2M2")
    plt.plot(dav1, qav1, 'r:' ,label = "R1M1")
    plt.plot( dav2, qav2, 'y' ,label = "R1M2")
    plt.plot(dav3, qav3, 'b:' ,label = "R2M1")
    plt.plot(dav4, qav4, 'g--',label = "R2M2")   
    plt.ylim(0, 0.7)
    plt.legend()
    plt.xlabel('density')
    plt.ylabel('flow')
    plt.title('Fundamental diagram: AV')
    plt.savefig("final/"+"/tricompav.pdf")    
    plt.show()
    '''
    plt.plot(range(len(l1)), l1  ,label = "R1M1") 
    plt.plot(range(len(l2)), l2  ,label = "R1M2")
    plt.plot(range(len(l3)), l3 ,label = "R2M1")
    plt.plot(range(len(l4)), l4 ,label = "R2M2")
    plt.xlabel('time steps')
    plt.legend()
    plt.ylabel('Number of lane changes to test lane')
    plt.savefig("final/"+"/lanecomprv.pdf")    
    plt.show()
    
    
    
    
    
plot2(r1m1, r1m2, r2m1, r2m2)    

"""
