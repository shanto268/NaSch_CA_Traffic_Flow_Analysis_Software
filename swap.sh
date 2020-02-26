cd simulation
echo in $PWD
mv car_def.py car0.py
python3 car0.py
echo Executed file
mv car0.py car_def.py
echo Restored file to original state!
cd ..
echo in $PWD
