#!/usr/bin/python

print '''Content-type:text/html

	<html>
		<head>
			<meta http-equiv=refresh content=0;url=http://10.129.200.50/cgi-bin/monitor/shwdata.py/>
		</head>'''
	

import cgi
import cgitb
cgitb.enable()
import MySQLdb

con=MySQLdb.connect(host='10.129.200.50',user='root',passwd='123',db='bndwidth')

cursor=con.cursor()
query1="delete from Analysis"
query2="delete from Packet_Percent"

cursor.execute(query1)
cursor.execute(query2)

con.commit()
cursor.close()
print "</html>"
