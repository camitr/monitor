#!/bin/bash

echo "Content-type: text/html"
echo ""
echo "<html><head>"

echo "	<meta http-equiv=refresh content=0;url=http://10.129.200.50/cgi-bin/monitor/shwdata.py/>"
echo "</head>"
echo "<body>"
echo "kill the process"
val=`cat pidpython`
 kill -9 $val
echo "</body>"
echo "</html>"
