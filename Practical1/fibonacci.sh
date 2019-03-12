printf "give no of terms\n"
read n
x=0
y=1
i=2
printf "Fibonacci Series up to $n terms : "
printf "$x "
printf "$y "
while [ $i -lt $n ]
do
	i=`expr $i + 1 `
	z=`expr $x + $y `
	printf "$z "
	x=$y
	y=$z
done
printf "\n"
