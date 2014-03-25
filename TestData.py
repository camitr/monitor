#!/usr/bin/python


import cgi,cgitb
import MySQLdb
from BaseHTTPServer import HTTPServer

print '''Content-Type: Text/html\n'''
print # to end the CGI response headers.
print '''<html>
		<head> 
	<!--		<meta http-equiv=refresh content=0;url=http://10.129.200.50/cgi-bin/monitor/shwdata.py>-->
		</head>'''
			
form=cgi.FieldStorage()
ID1=form.getvalue('ID')
total_machine=form.getvalue('total_machine')

oper_sys_1 =form.getvalue('os1')
oper_sys_2 =form.getvalue('os2')


if oper_sys_1:
	print	"<script>window.location='http://google.com'</script>>" 
if oper_sys_2:
	print	"<script>window.location='http://yahoo.com'</script>>" 

keyList = form.keys()

for key in keyList:
	if key ==form["os1"].value:
		print form["os1"].value + "<br>"
		#print key
#
print ID1
print oper_sys_1
print oper_sys_2
con=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',db='bndwidth')
cursor=con.cursor()

query="insert into Test_Details (date,Test_ID,No_Machine,OS) values('12-10-86',"+ID1+","+total_machine+",'"+str(oper_sys)+"');"

cursor.execute(query)
con.commit()
cursor.close()


print "</html>"
