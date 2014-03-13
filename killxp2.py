#!/usr/bin/python

import os
import psutil
from subprocess import Popen

#print "Content-Type: text/html\n\n"
#print "<html><head>"

#print "	<meta http-equiv=refresh content=0;url=http://10.129.200.50/cgi-bin/bndwidth/jstest/shwdata.py/>"
#print "</head>"

for process in psutil.process_iter():
	if process.cmdline==['sshpython.py']:
		print('Process found. Terminating it')
		process.terminate()
		break
	else:
		print("there is no process")
		print process
#print "</html>"

ab=os.getpid()
print ab
