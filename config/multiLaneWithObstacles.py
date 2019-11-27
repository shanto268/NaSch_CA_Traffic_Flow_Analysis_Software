from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1280, 720
# in miliseconds
updateFrame = 500

seed = None

lanes = 3
length = 83

maxSpeed = 5
maxLength = 1000

speedLimits = [SpeedLimit(range=((82, 0), (82, 2)), limit=0, ticks=0)] + [SpeedLimit(range=((20, 1), (50,1)), limit=0, ticks=0)]
trafficGenerator = SimpleTrafficGenerator(7)
slowDownProbability, laneChangeProbability = 0.3, 0.2
