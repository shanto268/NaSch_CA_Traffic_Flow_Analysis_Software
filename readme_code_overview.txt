==========================================================================================================================
CA Traffic Analysis Software

A pygame, numpy and matplotlib based software that lets you create simulation of different traffic flow scenarios using 
the concepts of Cellular Automata and perform data analysis and visualization.

Made by Sadman Ahmed Shanto in 2019
==========================================================================================================================


										*** Summary of files and directories ***

	The following outlines all the relevant directories and files for the software.

$$Base directory: This is the folder where all the directories are found.

>>> nagel.py
	
	This code is the initiator of the entire software. It starts the simulation engine running on pygame and returns control to the rest of the program files.

>>> representation.py

	This code is responsible for the visualization of the road, car, and information in the pygame window.

>>> infoDisplayer.py

	This code takes data from the back end of the software and displays that information on the pygame window by sending that data to the representation.py file. It also records all the parameters of interest in the text files.

>>> plot_exp1.py

	This code produces all the plots needed for experiment 1 from the raw data text file.

>>> plot_exp2.py

	This code produces all the plots needed for experiment 2 from the raw data text file.

>>> combined_plot_exp1.py

	This code makes plot that needs input from experiment 1 test cases using the raw text data files.

>>> simulationManager.py
	
	This code is responsible for updating the traffic flow simulations. It constantly transfers control back and forth from the car.py, road.py, representation.py and infoDisplayer.py file.


$$"config" directory: This directory holds files in charge of road/traffic situations.

>>> case.py

	This file describes the dimensions of the pygame window and the type of road/traffic condition to be simulated.


$$"Simulation" directory: This directory holds files that describe OOP code files.

>>> car.py

	This code creates an object called car with certain properties and functions that describes the vehicles behavior.

>>> road.py
	
	This code creates an object called road with certain properties and functions that describes the rules that vehicles interacting with the
road should abide by.

>>> speedLimits.py

	This code creates a provision to make traffic lights or damaged road conditions.

>>> trafficGenerators.py

	This code decides how traffic is generated in the simulation.

"draft_2" directory:

>>> contains all the raw data and results from the simulation experiments. 

---------------------------------------------------------------------------------------------------------------------------

										*** Control Flow of program: ***


		     .-> car.py  <----> road.py  <-.       <--------.	    
		     |				       |	             |				
	     .->[simulation object files(back end)]--> trafficGenerator.py		     .----------------------------> combined_plot_exp1.py
	     |                                   ^  			  ^ 			    /
case.py --> nagel.py					  |			  |----------> data.txt----------------------------> plot_exp1.py
	     |                                   |                |			    \
	     .->[visualization files(front end)] v			  |			     .----------------------------> plot_exp2.py	
	     |		       \  	     		|------------------|
	     |			  | 		simulationManager.py
	     |                   |  	       ^
	     v			   v	             |
  infoDisplayer.py <------> representation.py /
									  
								

*** How to run program (simulation): ***

	To run the simulation, be in the base directory and then in a python/linux/terminal shell use the following command:
$ python nagel.py config.case

*** How to run program (data visualization): ***

	To visualize data, you need to use one of .py files from the base directory which has the word "plot" in it. Make sure the the python file takes in the correct text data file as input from the right directory. To execute such a program use the following command:

$ python whatever_the_name_of_plot_file_you_want_to_use_is.py

---------------------------------------------------------------------------------------------------------------------------

										*** Next version: 1.1 ***

	The next version of the software would include a shell based front end that would take user inputs to make the process of simulation and data visualization more streamlined and easy to use.


