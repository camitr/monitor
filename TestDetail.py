#!/usr/bin/python


print'''Content-type:text/html\n'''
import cgi,cgitb
import MySQLdb

con=MySQLdb.connect(host='10.129.200.50',user='root',passwd='123',db='bndwidth')

cursor1=con.cursor()
cursor2=con.cursor()
cursor3=con.cursor()
query1="select name from PC_details;"
query2="select IP from PC_details;"
query3="Select OS from PC_details;"
cursor1.execute(query1)
cursor2.execute(query2)
cursor3.execute(query3)

con.commit()
#cursor.close()
rows1=cursor1.fetchall()
rows2=cursor2.fetchall()
rows3=cursor3.fetchall()


print'''<DOCTYPE html>
	<html>
	<head>
			<title>Start Test</title>
		</head>
			<body>
				<form action="TestDataSubmit.py" method="post">
					<div align=center>
					<H1>Test Details</H1>
					<table border=0 bgcolor=#A9F5F2>
						<tr>
						<td><b>Machine Name:</b></td><td>'''
output1 = ""
output1 += "<select name='o1'>"
for row in rows1:
	output1 += "<option value='{0}' name='o1'>{0} </option>".format(row[0] )
output1 += "</select>"

print output1
print'''						</td>
						<td>
						<b>	Start Time:</b><input type=time name='start' value"">
						</td>
						</tr>
						<tr>
						<td><b>IP:</b></td>
						<td>'''
output2 = ""
output2 += "<select name='o2'>"
for row in rows2:
	output2 += "<option value='{0}'>{0} </option>".format(row[0])
output2 += "</select>"
print output2
print'''						
						</td>
						<td>
						<b>	End Time:</b><input type=time name='end' value="">
						</tr>
						<tr>
						<td><b>OS:</b></td><td>'''
output2 = ""
output2 += "<select name='o3'>"
for row in rows3:
	output2 += "<option value='{0}' >{0}</option>".format(row[0])
output2 += "</select>"
print output2
						

print'''					</td>
						</tr>
						<tr>
						<td>
						</td>
						<td>
							
						<div align=center>
							<input type='submit' name='submit' value='submit'>	

						</div>
						</td>
						</tr>
						<tr>
						<td>'''
for row in rows1:
	output="<input type='checkbox' name='c1' value='{0}'>{0}".format(row[0])
print output
print'''					</table>
					</div>
				</form>
			</body>
	</html>'''


cursor1.close()
cursor2.close()
cursor3.close()


