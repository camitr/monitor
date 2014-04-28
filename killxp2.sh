#!/bin/bash

IFS=,
echo "Content-type: text/html"
echo ""
echo "<html><head>"

echo "	<meta http-equiv=refresh content=0;url=http://10.129.200.50/cgi-bin/monitor/TestDetailChckbox.py/>"
echo "</head>"
echo "<body>"
echo "kill the process"
for line in $(cat pidpython)
do
	
#val=`cat pidpython`
	val=$line
 	kill -9 $val
done

#rm -rf pidpython
echo "</body>"
echo "</html>"
