#!/usr/bin/python

print "Content-Type: text/html\n\n"

print '''<html>
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

#cur.execute("select * from Analysis having max(id)")
cur.execute("select * from Analysis where id in (select  max(id) from Analysis);")

rows=cur.fetchall()
print		'''<body> 	
			<table border-spacing:15px width=100% cellspacing=1 ><b>Live Bandwidth</b> \n
				<tr>
					<td>ID</td>
					<td>Date</td>
					<td>Machine</td>
					<td>IP</td>
					<td>TotalPacketUP</td>
					<td>AvgPacketUP</td>
					<td>AvgPacketSize</td>
					<td>BndwidthUP</td>
					<td>TotalPacketDwn</td>
					<td>AvgPacketDwn</td>
					<td>AvgPacketSizeDwn</td>
					<td>BwdthDwn</td></tr>\n'''
for row in rows:
	print "<tr>"
	print "<td bgcolor=#ffffff>"
	print  row[0]
	print "</td>"
	
	print "<td bgcolor=#00FF00>"
	print  row[1]
	print "</td>"



        print "<td bgcolor=#FF5353>"
        print  row[2]
        print "</td>"

	print "<td bgcolor=#CEB86C>"
        print  row[3]
        print "</td>"


        print "<td bgcolor=#66CCCC>"
        print  row[4]
        print "</td>"

        print "<td bgcolor=#00FFCC>"
        print  row[5]
        print "</td>"


        print "<td bgcolor=#999933>"
        print  row[6]
        print "</td>"

        print "<td bgcolor=#00FF99>"
        print  row[7]
        print "</td>"

        print "<td bgcolor=#669999>"
        print  row[8]
        print "</td bgcolor=#FF9966>"

        print "<td bgcolor=#999966>"
        print  row[9]
        print "</td>"

        print "<td bgcolor=#CC99FF>"
        print  row[10]
        print "</td>"


        print "<td bgcolor=#99CCFF>"
        print  row[11]
print'''	</td>
        	</tr>

			</table>

		</body>
	</html>'''

