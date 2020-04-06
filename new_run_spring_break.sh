echo FD Base 1
. fd_sim_case.sh fd_base_hway.txt 15 5 4 4 3 0.6 0.6 0.4 0.4 car_base.py
echo FD Base 2
. fd_sim_case.sh fd_base_hvlike.txt 15 5 3 3 3 0.6 0.6 0.4 0.4 car_base.py

echo Static Case 1
. run_base_hway.sh
echo Static Case 2
. run_base_hvlike.sh
echo 
echo Done!
