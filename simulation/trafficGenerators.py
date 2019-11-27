import random
import numpy as np
import math as mp
import simulation.road
#class that generates traffic with real life distributions
class SimpleTrafficGenerator():
    def __init__(self, carPerUpdate=1): #number of cars to be generated per update
        self.queue = 0
        self.carPerUpdate = carPerUpdate
        #print(" Car per update: " + str(carPerUpdate))
    def generate(self, road):
        amount = random.randint(0, self.carPerUpdate) 
        print(" Amount: " + str(amount))
        self.tryGenerate(road, amount)         
    
    def tryGenerate(self, road, amount):
        added = road.pushCarsRandomly(amount + self.queue)
        print(" Added: " + str(added))
        self.queue += (amount - added)
                                                                                  

                                                                                                   
class TrafficGenerator():
    def __init__(self, carPerUpdate=1): #number of cars to be generated per update
        self.carPerUpdate = carPerUpdate
        self.counter = 0     
                                                      
    def generate(self, road):
        self.counter += 1
        amount = self.carPerUpdate * self.counter
      #  mu, sigma = amount, mp.sqrt(amount) # mean and standard deviation
   #     incoming = np.random.normal(mu, sigma, 100) 
   #     for i in range(len(incoming)):
   #         if incoming[i] <= 0:
    #            incoming[i] = random.randint(1,9)
       
   #     x =random.randint(0,99)
    #    prob_in = round(incoming[x])
      #  print(self.counter)
        self.tryGenerate(road, amount)         
        
    def tryGenerate(self, road, prob_in): #change necessary here when incrementing gradual increase in flow
        added = road.pushCars(prob_in)
        road.inflow(added)
    #    if added < 3:
          #  print(incoming)
            
        
        
        
        
        
        