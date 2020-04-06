# simulates all increasing case situations
#

echo Aware Model Simulation
echo
. fd_sim_case.sh fd_aware.txt 15 5 5 4 3 0.6 0.6 0.4 0.4 car_h.py

echo Aware and Opportunistic Model Simulation
echo
. fd_sim_case.sh fd_aware_oppo.txt 15 5 5 4 3 1 0.6 0 0.4 car_h.py

echo Base Scenario Headway Model Simulation
echo
. fd_sim_case.sh fd_base_hway.txt 15 4 4 4 3 0.6 0.6 0.4 0.4 car_base.py

echo Base Scenario HV Like Model Simulation 
echo
. fd_sim_case.sh fd_base_hvlike.txt 15 3 3 3 3 0.6 0.6 0.4 0.4 car_base.py

echo Opprtunistic Model Simulation
echo
. fd_sim_case.sh fd_oppo.txt 15 4 4 4 3 1 0.6 0 0.4 car_nh.py

echo
echo Done Simulation
