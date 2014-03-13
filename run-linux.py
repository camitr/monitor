#!/usr/bin/python

print "Content-Type: text/html\n\n"

import cgi
import cgitb
cgitb.enable()
import MySQLdb as mdb
import subprocess

form = cgi.FieldStorage()

print "<html>"
print "<head>"
print "	<meta http-equiv=refresh content=0;url=http://10.129.200.50/cgi-bin/monitor/shwdata.py/>"

subprocess.Popen("./infyloop.sh",shell=True)

print "</head>"
print "</html>"

















