#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

"""
config_dir = '/Users/ttumuon/muonSC8/sas/Python_new/config/'
sim_dir = '/Users/ttumuon/muonSC8/sas/Python_new/simulation/'
base_dir = '/Users/ttumuon/muonSC8/sas/Python_new/'
"""

config_dir = 'config/'
sim_dir = 'simulation/'
base_dir = ''


""" The following is code for config directory """
#*************************************** CASE ***************************************

# Read in the file
with open( config_dir + 'case.py', 'r') as file :
  filedata = file.read()

#default values
dlanes = 3
dlength = 100
dnumcars = 50

#user input values
nlanes = 5
nlength = 200
nnumcars = 100

# Replace the target string
filedata = filedata.replace('lanes = ' + str(dlanes), 'lanes = '+str(nlanes))
filedata = filedata.replace('length = '+ str(dlength) , 'length = '+ str(nlength))
filedata = filedata.replace('trafficGenerator = TrafficGenerator('+str(dnumcars)+')', 'trafficGenerator = TrafficGenerator('+str(nnumcars)+')' )
# Write the file out again
with open( config_dir + 'case.py', 'w') as file:
  file.write(filedata)

#====================================================================================

""" The following is code for simulation directory """

#*************************************** ROAD ***************************************

# Read in the file
with open( sim_dir + 'road.py', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('lanes = 3', 'lanes = 5')
filedata = filedata.replace('length = 100', 'length = 200')

# Write the file out again
with open( config_dir + 'road.py', 'w') as file:
  file.write(filedata)
  

#*************************************** CAR ***************************************

# Read in the file
with open( sim_dir + 'car.py', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('lanes = 3', 'lanes = 5')
filedata = filedata.replace('length = 100', 'length = 200')

# Write the file out again
with open( config_dir + 'car.py', 'w') as file:
  file.write(filedata)


#*************************************** TRAFFIC GENERATOR *************************

# Read in the file
with open( sim_dir + 'trafficGenerators.py', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('lanes = 3', 'lanes = 5')
filedata = filedata.replace('length = 100', 'length = 200')

# Write the file out again
with open( config_dir + 'trafficGenerators.py', 'w') as file:
  file.write(filedata)

#====================================================================================
  
""" The following is code for base directory """

#*************************************** NAGEL ***************************************

# Read in the file
with open( base_dir + 'nagel.py', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('lanes = 3', 'lanes = 5')
filedata = filedata.replace('length = 100', 'length = 200')

# Write the file out again
with open( config_dir + 'nagel.py', 'w') as file:
  file.write(filedata)
  
#*************************************** REPRESENTATION ***************************************

# Read in the file
with open( base_dir + 'representation.py', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('lanes = 3', 'lanes = 5')
filedata = filedata.replace('length = 100', 'length = 200')

# Write the file out again
with open( config_dir + 'representation.py', 'w') as file:
  file.write(filedata)

#*************************************** SIMULATION MANAGER ***************************************

# Read in the file
with open( base_dir + 'simulationManager.py', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('lanes = 3', 'lanes = 5')
filedata = filedata.replace('length = 100', 'length = 200')

# Write the file out again
with open( config_dir + 'simulationManager.py', 'w') as file:
  file.write(filedata)
  
#*************************************** INFO DISPLAYER ***************************************

# Read in the file
with open( base_dir + 'infoDisplayer.py', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('lanes = 3', 'lanes = 5')
filedata = filedata.replace('length = 100', 'length = 200')

# Write the file out again
with open( config_dir + 'infoDisplayer.py', 'w') as file:
  file.write(filedata)


#*************************************** PLOT EXP 1 ***************************************

# Read in the file
with open( base_dir + 'plot_exp1.py', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('lanes = 3', 'lanes = 5')
filedata = filedata.replace('length = 100', 'length = 200')

# Write the file out again
with open( config_dir + 'plot_exp1 .py', 'w') as file:
  file.write(filedata)
  


#=====================================================================================
