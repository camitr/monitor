#!/usr/bin/python

print '''Content-Type: text/html\n\n

	<html>
		<head>
		<meta http-equiv=refresh content=2>
		</head>'''
import cgi
import cgitb
cgitb.enable()
import MySQLdb as mdb

form = cgi.FieldStorage()
keyword = form.getvalue('keyword')

conn=mdb.connect(host='10.129.200.50',user='root',passwd='123',db='bndwidth') 
cur=conn.cursor()

#cur.execute("select * from Packet_Percent order by ID desc ")
#cur.execute("select * from Packet_Percent_Server order by ID desc ")
#cur.execute("select * from Packet_Percent_Server having max(id) ")
cur.execute("select * from Packet_Percent_Server where id in (select  max(id) from Packet_Percent_Server); ")

rows=cur.fetchall()

print'''	<body>
			<table border-spacing:15px width=100% cellspacing=0 > \n
				<tr>
					<td>ID</td>
					<td>Machine</td>
					<td>IP</td>
					<td>40-79</td>
					<td>80-159</td>
					<td>160-319</td>
					<td>320-639</td>
					<td>640-1279</td>
					<td>1280-2559</td>
					<td>2560-5119</td>
				</tr>\n'''
for row in rows:
	print "<tr>"
	print "<td bgcolor=#ffffff>"
	print  row[0]
	print "</td>"
	
	print "<td bgcolor=#FF5353>"
	print  row[1]
	print "</td>"



        print "<td bgcolor=#CEB86C>"
        print  row[2]
        print "</td>"
	
	print "<td bgcolor=#D8BFD8>"
        print  row[3]
        print "</td>"


        print "<td bgcolor=#708090>"
        print  row[4]
        print "</td>"

        print "<td bgcolor=#F5DEB3>"
        print  row[5]
        print "</td>"


        print "<td bgcolor=#B0E0E6>"
        print  row[6]
        print "</td>"

        print "<td bgcolor=#F08080>"
        print  row[7]
        print "</td>"

        print "<td bgcolor=#8FBC8F>"
        print  row[8]
        print "</td bgcolor=#FF9966>"

        print "<td bgcolor=#999966>"
        print  row[9]
print'''	</td>
	</tr>
			</table>

		</body>
	</html>'''



















