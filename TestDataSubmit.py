#!/usr/bin/python

import cgi,cgitb
import MySQLdb
from contest import DbConnect

#con=MySQLdb.connect(host='10.129.200.50',user='root',passwd='123',db='bndwidth',)
#cursor = con.cursor()

print'''Content-type: text/html\n'''
print'''	<html>
		<head>
		</head>
	'''
form=cgi.FieldStorage()

O1=form.getvalue('c1')
#print O1
#print "Length=",len(O1)

O2=form.getvalue('o2')
O3=form.getvalue('o3')
t1=form.getvalue('start')
t2=form.getvalue('end')
#print O2
#print t1
data=''.join(O1)

print data
query1="Insert into Test_Start_Detail (Start,End) values('"+(t1)+"','"+(t2)+"');"
#cursor.execute(query1)
#i=cursor.lastrowid
con=DbConnect()

res=con.execute(query1)
i=con.lastrowid()
print "id=",i

for l in range(len(O1)):
	query2="insert into Test_Pc_Detail (Test_id,PC) values('"+str(i)+"','"+str(data)+"')" 


con.execute(query2)
#cursor.execute(query2)
#con.commit()
#cursor.close()
print "</html>"
