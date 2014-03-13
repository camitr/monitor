#!/bin/bash

while :
do	
	echo "Press [Ctrl+c] to stop.."
	sleep 3

	./looptest.sh

echo $$>pid
done

