#Usage of code python3 nagel.py name_of_data_text_file.txt number_of_cars max_speed
# $1 = rawdata.txt
# $2 = number of cars
# $3 = max speed on the road
# $4 = max speed of AV (AV-AV)
# $5 = AV-HV speed
# $6 = max speed of HV 
# $7 = Probability of lane change of AV
# $8 = Probability of lane change of HV
# $9 = Probability of braking of AV
# $10 = Probability of braking of HV
# 
#           NOT IMPLEMENTED YET
# ~~~~~~~~~~~~~~~~~ Optional ~~~~~~~~~~~~~~~~
# $11 = Probability of AV
# $12 = Number of lanes
# $13 = Number of Cells in a lane
# $14 = Simulation time
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#change car.py
cd simulation
mv car_nh.py car.py
echo "The chosen AV model is Base Scenario (HV Like)"
echo
cd ..

#different density simulations
echo Low density regime: 0.08
python3 nagel.py low_density_base_hv_like.txt 24 5 3 3 3 0.6 0.6 0.4 0.4
echo 
echo Simultation is complete!
echo Critical density regime: 0.2
python3 nagel.py crit_density_base_hv_like.txt 60 5 3 3 3 0.6 0.6 0.4 0.4
echo 
echo Simultation is complete!
echo High density regime: 0.6
python3 nagel.py high_density_base_hv_like.txt 180 5 3 3 3 0.6 0.6 0.4 0.4
echo 
echo Simultation is complete!
echo

#change back car files
cd simulation
mv car.py car_nh.py
echo Simulation files restored
echo
cd ..
echo All simulation cases for Base Scenario - HV like - model is over

#echo Executing analysis files now....
# execute plot files
#echo Analysis plots created!

