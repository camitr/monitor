#!/usr/bin/python

print "Content-Type: text/html\n\n"
print ''' <!DOCTYPE html>
	 <html lang=en>
		<head>
			<meta charset=utf-8>
			<title>Bandwidth Monitor</title>
		</head>
	'''

import cgi
import cgitb
cgitb.enable(display=0, logdir="/var/www/cgi-bin/monitor/logdir")
#import MySQLdb as mdb
import MySQLdb

con=MySQLdb.Connect(host='127.0.0.1',user='root',passwd='123',db='bndwidth')
cur=con.cursor()
query1="select Name from PC_details"
cur.execute(query1)
con.commit()
row=cur.fetchall()

re=[elem[0] for elem in row]

print re
pc1=re[4]
print pc1
print "<body><table border=1>"
for pc in row:
	print "<tr><td><form name=pc action=/cgi-bin/monitor/sshpython.py method=post/ target='_blank'><input type=submit name=pc value={0}></td></tr>".format(pc[0])

