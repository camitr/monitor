#!/usr/bin/python

print '''Content-Type: text/html\n\n'''
print'''<html><head>
	<meta http-equiv=refresh content=0;url=http://10.129.200.50/cgi-bin/monitor/TestDetailChckbox.py/>
	</head>
'''
import os
import paramiko
import MySQLdb
import cgi,cgitb
cgitb.enable()
con=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',db='bndwidth')
cursor=con.cursor()

query1="select Name from PC_details"
cursor.execute(query1)
con.commit()

row=cursor.fetchall()
re=[elem[0] for elem in row]

form=cgi.FieldStorage()
pc=form.getvalue('pc')
query2="select IP,User,Password  from PC_details where Name='"+str(pc)+"'"


for i in range(len(re)):
#	print re[i]
	if re[i]==pc:
		print "match"
		cursor.execute(query2)
		con.commit()
		ip=cursor.fetchall()
		#ip=[elem[0] for elem in ip]
		ip=ip[0]
		user=ip[1]
		pwd=ip[2]
		print ip[1]
print pc

pidp=os.getpid()
print pidp
f=open('pidpython','a')


f.write(str(pidp) + ",")
f.close()
print pc
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy())
#ssh.connect(ip[0],username='admin',password='ttt23$')
ssh.connect(hostname=ip[0],username=ip[1],password=ip[2])
print "Analysing the packets......."
stdin,stdout,stderr=\
ssh.exec_command("./infyloop.sh")
type(stdin)
out=stdout.readlines()
print out

print"</html>"

#ssh.exec_command("ls")

