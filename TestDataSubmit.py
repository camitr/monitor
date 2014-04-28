#!/usr/bin/python

import cgi,cgitb
import MySQLdb
from contest import DbConnect


print'''Content-type: text/html\n'''
print'''	<html>
			<meta http-equiv=refresh content=0;url=http://10.129.200.50/cgi-bin/monitor/TestDetailChckbox.py>
		<head>
		</head>
	'''

def main():
	form=cgi.FieldStorage()
	pc_name=form.getvalue('c1')
	O2=form.getvalue('o2')
	O3=form.getvalue('o3')
	t_start=form.getvalue('start')
	t_end=form.getvalue('end')
	print pc_name
	database(t_start,t_end,pc_name)
	print "</html>"

def database(t_start,t_end,pc_name):

	data=''.join(pc_name)
	query1="Insert into Test_Start_Detail (Start,End) values('"+(t_start)+"','"+(t_end)+"');"
	con=DbConnect()
	res=con.execute(query1)
	row_id=con.lastrowid()
	print "id=",row_id
	for i in range(len(pc_name)):
		query2="insert into Test_Pc_Detail (Test_id,PC) values('"+str(row_id)+"','"+str(data)+"')" 
	con.execute(query2)
	


if __name__=="__main__":main()

