import simulation.road, simulation.speedLimits
from simulation.speedLimits import *
from simulationManager import SimulationManager
from simulation.trafficGenerators import *
from infoDisplayer import *

maxFps= 40
size = width, heigth = 1280, 800
# in miliseconds
updateFrame = 500

seed = None

lanes = 3
length = 83

trafficGenerator = SimpleTrafficGenerator(10)
slowDownProbability, laneChangeProbability = 0.3, 0.2

speedLimits = []

road = simulation.road.Road(lanes, length, speedLimits)
simulation = SimulationManager(road, trafficGenerator, updateFrame)
maxSpeed = 5
maxLength = 1000

class Params():
    
    def __init__(self, road, simulationManager):  
        
        self.road = road
        self.simulationManager = simulationManager
        self.cells = road.getCellCount()
        self.timeFactor = 0
        
    def density(self):
        carNum = self.road.carCount()
        density = carNum/self.cells
        print ("density: {:0.3f}".format(density))
        return(density)
            
    def carNum(self):
        carNum = self.road.carCount()
        print("car count: " + str(carNum))
        return(carNum)

d = Params(road, simulation)
rho = d.density()
num = d.carNum()
print("car count: " + str(num))

speedLimits = [ SpeedLimit(range=((82, 0), (82,3)), limit=0, ticks=0)]+[ SpeedLimit(range=((0, 1), (82,1)), limit=2, ticks=0)]

#print ("density: {:0.3f}".format(rho))

'''
if rho > 0.25:
    speedLimits = [ SpeedLimit(range=((82, 0), (82,3)), limit=0, ticks=0)]+[ SpeedLimit(range=((0, 1), (82,1)), limit=2, ticks=0)]
else:
    speedLimits = [ SpeedLimit(range=((82, 0), (82,3)), limit=0, ticks=0)]+[ SpeedLimit(range=((0, 2), (82,2)), limit=2, ticks=0)]    
#elif infoDisplayer.InfoDisplayer.update.congestion < 2.5:
#    speedLimits = [ SpeedLimit(range=((20, 3), (40,3)), limit=0, ticks=0)]

'''
