import simulation.road, simulation.speedLimits
import random
import sys
from simulation.speedLimits import *
from simulation.trafficGenerators import *
#from simulationManager import SimulationManager
#from infoDisplayer import *
#from density import *

#avpercent = sys.argv[1]

maxFps= 500 #default = 40 , fast = 10, nice = 500
size = width, heigth = 1600, 600
# in miliseconds
updateFrame = 500 #default = 500, fast = 10 , nice 500

seed = None

lanes = 3
length = 100

#trafficGenerator = SimpleTrafficGenerator(10)
trafficGenerator = TrafficGenerator(10) #density 0.08= 24, 0.2 = 60, 0.6 = 180     #if 10 then that means increase system density linearly
#trafficGenerator = GaussianTrafficGenerator(15,25) #Needs A LOT OF WORK!
speedLimits = []

maxSpeed = 5
maxLength = 1000
l = 139
ti = 20

t = random.randint(7,13)

slowDownProbability, laneChangeProbability = 0,0

#traffic lights
#speedLimits = [SpeedLimit(range=((l , 0), (l ,3)), limit=0, ticks=60, active = True)]


#boundary fixed
#speedLimits = [SpeedLimit(range=((l , 0), (l ,3)), limit=0, ticks=0, active = True)]

#blinking entry and traffic lights
#speedLimits = [SpeedLimit(range=((7, 0), (7,3)), limit=0, ticks=t, active = True)] + [SpeedLimit(range=((l , 0), (l ,3)), limit=0, ticks=100, active = True)] #tick = non_zero_number = traffic light

#blinking entry and closed
#speedLimits = [SpeedLimit(range=((7, 0), (7,3)), limit=0, ticks=t, active = False)] + [SpeedLimit(range=((l , 0), (l ,3)), limit=0, ticks=0, active = True)] #tick = non_zero_number = traffic light

























'''

road = simulation.road.Road(lanes, length, speedLimits)
simulation = SimulationManager(road, trafficGenerator, updateFrame)
param = Params(road,simulation)
v = param.prob()

def prob():
        w = random.randint(1,2)      
        print(" ")
        if w == 1: #determines degree of mixed flow
            slowDownProbability, laneChangeProbability = 0.3, 0.4
            print("P(RV slow down): %s " % str(slowDownProbability))
            print("P(RV lane change): %s " % str(laneChangeProbability))#case: RV
        else:
            slowDownProbability, laneChangeProbability = 0, 0 #case: AV
            print("P(AV slow down): %s " % str(slowDownProbability))
            print("P(AV lane change): %s " % str(laneChangeProbability))
        print(" ")
        return slowDownProbability, laneChangeProbability;

ps, pl = prob()
print(ps)
print(pl)
'''















'''
while (True):
    f = random.randint(1,11)
    if f > 5: #time based loop using ticks 
        speedLimits = [ SpeedLimit(range=((0, 2), (l,2)), limit=2, ticks=t, active=False)] 
    else:
        speedLimits = [ SpeedLimit(range=((0, 1), (l,1)), limit=2, ticks=t, active=False)] 
\

class density:
    def rho(self):
        rho = InfoDisplayer.update(self)

t = density()
t.rho
print (t.rho)

class Params():
    
    def __init__(self, road, simulationManager):  
        
        self.road = road
        self.simulationManager = simulationManager
        self.cells = road.getCellCount()
        self.timeFactor = 0
        
    def density(self):
        carNum = self.road.carCount()
        density = carNum/self.cells
        return(density)
            
    def carNum(self):
        carNum = self.road.carCount()
        #print("car count: " + str(carNum))
        return(carNum)


def density():
    cells = road.getCellCount()
    carNum = road.carCount()
    density = carNum/cells
    return(density)
    print ("density: {:0.3f}".format(density))

density()
'''

#speedLimits = [ SpeedLimit(range=((82, 0), (82,3)), limit=0, ticks=0)]+[ SpeedLimit(range=((0, 1), (82,1)), limit=2, ticks=0)]

#print ("density: {:0.3f}".format(rho))

'''
if rho > 0.25:
    speedLimits = [ SpeedLimit(range=((82, 0), (82,3)), limit=0, ticks=0)]+[ SpeedLimit(range=((0, 1), (82,1)), limit=2, ticks=0)]
else:
    speedLimits = [ SpeedLimit(range=((82, 0), (82,3)), limit=0, ticks=0)]+[ SpeedLimit(range=((0, 2), (82,2)), limit=2, ticks=0)]    
#elif infoDisplayer.InfoDisplayer.update.congestion < 2.5:
#    speedLimits = [ SpeedLimit(range=((20, 3), (40,3)), limit=0, ticks=0)]

'''
