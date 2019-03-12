echo "Enter first number"
read x;

echo "Enter second number"
read y;

if [ $x = $y ]
then
  echo "both are equal";
elif [  $x -gt $y ]
then
  echo "$x is greater";
else
  echo "$y is greater";
fi
