#!/usr/bin/python


print'''Content-type:text/html\n'''
import cgi,cgitb
import MySQLdb

con=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',db='bndwidth')

cursor1=con.cursor()
query1="select * from PC_details;"
cursor1.execute(query1)

con.commit()

rows1=cursor1.fetchall()


count=0
print'''<DOCTYPE html>
	<html>
	<head>
			<title>Start Test</title>
		</head>
			<body bgcolor="B0D6A9" >
				<table border=1 align=center cellspacing=0>
				<tr>
				<td bgcolor=EDBBC6>
					<div>
						<table border=0 bgcolor=EDBBC8>
						<div style='margin-top:10px'>
							<H1>Links</H1>
						</div>
						<tr><td>
							<a href="http://10.129.200.50/cgi-bin/monitor/PcDetails.py"</a>ADD PC</td></tr>
						<tr><td>
							<a href="http://10.129.200.50/cgi-bin/monitor/shwband.py" target='_blank'</a>Current Bandwidth</td></tr>
						<tr><td>
							<a href="http://10.129.200.50/cgi-bin/monitor/ShwPcktDwn.py" target='_blank'</a>Current Download Packet Percent</td></tr>
						<tr><td>
							<a href="http://10.129.200.50/cgi-bin/monitor/shwpckt.py" target='_blank'</a>Current Upload Packet Percent</td></tr>
						</table>
					</div>
				</td>
				<td bgcolor=E8A5B0>
				<form action="TestDataSubmit.py" method="post">
					<div align=center>
						<H1>Test Details</H1>
						<table border=0  bgcolor=E8A5B0>
						<tr>	<td><b>Machine Name:</b></td>
							<td align=center><b>IP :</b></td>
							<td></td>
							<td><b>Operating System :</b></td>
							<div id="count" >'''

print '''						</td></div>
'''
print "						<p>Select Machine to conduct the test </p>"

for row in rows1:

	count+=1
	output="<input type='checkbox' name='c1' value='{0}' checked onclick=enable(this.checked,'ifm1')>{0}".format(row[1])
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
						<table border=1 >
						<tr>
							<div align="right">	
							<td>
								<b>	Start Time:</b><input type=time name='start'  value"">
							</td>
							<td></td>
							<td></td>
							<td>
								<b>	End Time:</b><input type=time name='end' value="">
						</tr>
							</div>
							<tr></td></tr>	
								<td></td>
								<td>		
								<div align=left>
									<input type='submit' name='submit' value='submit'>								</div>
								</td>
							</tr>
			<tr>
						</table>
<!--<iframe id='ifm1' style='display:none' src=http://10.129.200.50/cgi-bin/monitor/TestRun.py width=100% height=100%></iframe>-->
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
	</td>
	</tr>
	</table>
'''
print'''<div align=center> <table>
	<tr><td>'''
print "<b>Click on the button  to Run the test for  selected PC</b>"
print "</td></tr><tr><td>"
for pc in rows1:
	print "<tr><form name=pc action=/cgi-bin/monitor/sshpython.py method=post /><input type=submit name=pc value={0}></tr>".format(pc[1])

print''' </form></td></tr>
<tr><td align=center>

<b>Click on button to stop monitoring</b>
 <form action=/cgi-bin/monitor/killxp2.sh method=post/>
                                        <td>
                                                <button type=submit autofocus style='width=48;height=60;background-color:#98FB98'>Stop Monitoring</button>
</td></tr>
</form>
	</table></div></body>
	</html>'''


cursor1.close()


