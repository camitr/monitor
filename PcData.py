#!/usr/bin/python

import cgi,cgitb
cgitb.enable()
from contest import DbConnect

print '''Content-type: text/html \n'''


form=cgi.FieldStorage()
PC=form.getvalue('PC')
IP=form.getvalue('IP')
OS=form.getvalue('OS')
USR=form.getvalue('user')
PWD=form.getvalue('password')


query="insert into PC_details (Name,IP,OS,User,Password) values('"+str(PC)+"','"+str(IP)+"','"+str(OS)+"','"+str(USR)+"','"+str(PWD)+"');"

foo = DbConnect()
res = foo.execute(query)
if res:
	print "updated"
else:
	print "failed"
