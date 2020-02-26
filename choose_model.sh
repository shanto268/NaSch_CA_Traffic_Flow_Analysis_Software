# elif statements
if [ $1 == 'a' ]
then
echo Aware model
elif [ $1 == 'o' ]
then
echo Opportunistics model
elif [ $1 == 'ao' ] || [ $1 == 'oa' ] 
then
echo Aware and Opportunistic
elif [ $1 == 'b1' ]
then
echo Base Scenario model 1
elif [ $1 == 'b2' ]
then
echo Base Scenario model 2
else
echo "Please choose a model: {a,o,ao,b1,b2}"
fi
