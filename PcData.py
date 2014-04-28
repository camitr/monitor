#!/usr/bin/python

import cgi,cgitb
cgitb.enable()
from contest import DbConnect

print '''Content-type: text/html \n\n'''

print	'''<html> 
	<head>
		<meta http-equiv=refresh content=0;url=http://10.129.200.50/cgi-bin/monitor/TestDetailChckbox.py/>
	</head>'''
form=cgi.FieldStorage()
PC=form.getvalue('PC')
IP=form.getvalue('IP')
OS=form.getvalue('OS')
USR=form.getvalue('user')
PWD=form.getvalue('Password')
print PWD

query="insert into PC_details (Name,IP,OS,User,Password) values('"+str(PC)+"','"+str(IP)+"','"+str(OS)+"','"+str(USR)+"','"+str(PWD)+"');"

foo = DbConnect()
res = foo.execute(query)
if res:
	print "updated"
else:
	print "failed"

print"</html>"
