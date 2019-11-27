import simulation.road, simulation.speedLimits
import random
from simulation.speedLimits import *
from simulation.trafficGenerators import *
#from simulationManager import SimulationManager
#from infoDisplayer import *
#from density import *


maxFps= 10 #default = 40 , fast = 10, nice = 500
size = width, heigth = 1800, 400
# in miliseconds
updateFrame = 10 #default = 500, fast = 10 , nice 500

seed = None

lanes = 3
length = 238

trafficGenerator = SimpleTrafficGenerator(10)

speedLimits = []

maxSpeed = 5
maxLength = 1000
l = 118
ti = 20

slowDownProbability, laneChangeProbability = 0,0

 
#big road two traffic lights: 
#speedLimits = [SpeedLimit(range=((40, 0), (40,3)), limit=0, ticks=20, active = True)] + [SpeedLimit(range=((2*l + 1 , 0), (2*l + 1 ,3)), limit=0, ticks=150, active = False)] #tick = non_zero_number = traffic light

#big road two traffic lights closed:  
#speedLimits = [SpeedLimit(range=((40, 0), (40,3)), limit=0, ticks=30, active = True)] + [SpeedLimit(range=((2*l + 1 , 0), (2*l + 1 ,3)), limit=0, ticks=0, active = True)] #tick = non_zero_number = traffic light

#big road one traffic light closed: 
#speedLimits = [SpeedLimit(range=((2*l + 1 , 0), (2*l + 1 ,3)), limit=0, ticks=0, active = True)] #tick = non_zero_number = traffic light

#big road one traffic light blinking: 
speedLimits = [SpeedLimit(range=((2*l + 1 , 0), (2*l + 1 ,3)), limit=0, ticks=60, active = True)] #tick = non_zero_number = traffic light

