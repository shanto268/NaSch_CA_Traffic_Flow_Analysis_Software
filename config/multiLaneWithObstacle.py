from simulation.speedLimits import *
from simulation.trafficGenerators import *

maxFps= 40
size = width, heigth = 1280, 800
# in miliseconds
updateFrame = 500

seed = None

lanes = 3
length = 83



maxSpeed = 5
maxLength = 1000
#if infoDisplayer.InfoDisplayer.update.congestion > 2.5:
speedLimits = [ SpeedLimit(range=((82, 0), (82,3)), limit=0, ticks=0)]
#speedLimits = [ SpeedLimit(range=((30, 1), (60,1)), limit=0, ticks=0)]
#elif infoDisplayer.InfoDisplayer.update.congestion < 2.5:
#    speedLimits = [ SpeedLimit(range=((20, 3), (40,3)), limit=0, ticks=0)]
trafficGenerator = SimpleTrafficGenerator(10)
slowDownProbability, laneChangeProbability = 0.3, 0.2

