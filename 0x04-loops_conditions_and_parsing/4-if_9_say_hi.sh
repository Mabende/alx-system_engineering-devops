#!/usr/bin/env bash
# display using while and if 
 
counter=1
while (( counter <= 10 ));
do
	echo "Best School"
	if (( counter == 9 ));
	then	
		echo "Hi"
	fi
	((counter++))
done
