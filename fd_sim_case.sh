# simulates a specific case for increasing density
# inputs $1 ... $10 for regular inputs for the sim case
# input $11 determines the car.py file used


#change og simulationManager.py to a garbage state 
mv simulationManager.py simulationManager.pydefault

#make simulationManager_increasing.py main simulationManager.py
mv simulationManager_increasing.py simulationManager.py
echo Changed SimManager
echo 
#change road file
cd simulation
mv road.py road.pydefault
mv road_increasing.py road.py
echo Changed road
echo 
#execute all sim cases for car_h.py dependent files
mv ${11} car.py
echo Changed car
echo 
cd ..
#execute aware file
echo Test start! 
echo 
python3 nagel.py $1 $2 $3 $4 $5 $6 $7 $8 $9 ${10}

#restore everything to default state
mv simulationManager.py simulationManager_increasing.py
mv simulationManager.pydefault simulationManager.py
echo Changed SimManager back
echo 

cd simulation
mv road.py road_increasing.py
mv road.pydefault road.py
echo Changed road back
echo 
mv car.py ${11}
echo Changed car back
echo 
cd ..
echo

