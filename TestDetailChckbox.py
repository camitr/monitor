#!/usr/bin/python


print'''Content-type:text/html\n'''
import cgi,cgitb
import MySQLdb

con=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',db='bndwidth')

cursor1=con.cursor()
cursor2=con.cursor()
cursor3=con.cursor()
query1="select * from PC_details;"
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

count=0
print'''<DOCTYPE html>
	<html>
	<head>
			<title>Start Test</title>
		</head>
			<body bgcolor="#BFBFBF">
				<form action="TestDataSubmit.py" method="post">
					<div align=center>
					<H1>Test Details</H1>
					<table border=0 >
						<tr>
						<td><b>Machine Name:</b></td>
						<td align=center><b>IP:
							</b></td>
						<td></td>
						<td><b>Operating System:</b></td>
						<div id="count" >'''
#for row in rows2:
#	count+=1
#	output2 = format(row[0])
#	print output2
#					

print '''					</td></div>
'''
print "<p>Select Machine to conduct the test </p>"

for row in rows1:
	
	count+=1
	output="<input type='checkbox' name='c1' value='{0}' checked onclick=enable(this.checked,'count')>{0}".format(row[1])
	print "<tr>"
	print "<td>"
	print output
	print "<td>"
	print row[2]
	print "</td><td></td>"
	
	print "<td>"
	print row[3]
	print "</td>"
	print "</td>"
	print "</tr>"

print'''				</table>
					<table border=0 >
						<div align="right">	
						<td>
						<b>	Start Time:</b><input type=time name='start'  value"">
						</td>
						<td>
						</td>
						<td></td>


						<td>
						<b>	End Time:</b><input type=time name='end' value="">
						</tr>
						</div>
						
						

				
						<tr>
						</td>
						</tr>	
						<td>
						</td>
						<td>		
						<div align=left>
							<input type='submit' name='submit' value='submit'>	

						</div>
						</td>
						</tr>
						<tr>
						
					</table>
					</div>
					<script language='JavaScript'>
                               	 		function enable(isEnable,os){
                                        		if (isEnable==false)
                                                		document.getElementById(os).style.display='none';
                                        		else
                                                		document.getElementById(os).style.display='inline';

                                                                		}
                        </script>    
				</form>
			</body>
	</html>'''


cursor1.close()
cursor2.close()
cursor3.close()


