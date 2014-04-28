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
print '''
		 <body>
			<table border=0 width=100% height=50% cellspacing=0 >
				<tr>
					<td><b>XP Client Bandwidth</b>
					<!--	<h2>Upload & Download Bandwidth of XP Clients:Kbps</h2>-->
					<iframe src=http://10.129.200.50/cgi-bin/monitor/ShwDataXp.py  width=100% height=100% ></iframe>
					</td>
				</tr>
			</table>
	
			<table border=1 width=100% height=100% bgcolor=#6666CC>

				</tr>
				<form action=/cgi-bin/monitor/sshpython.py method=post/>
					<td>
						<input type=submit name=pc1 value={0} autofocus style='width=48;height=60;background-color:#98FB98' >'''.format(re[4]) 
#print "i hv=",name
print'''				</form>
					</td>


				<form action=/cgi-bin/monitor/killxp2.sh method=post/>
					<td>
						<button type=submit autofocus style='width=48;height=60;background-color:#98FB98'>kill XP2</button>
					</td>
				</form>

				</tr>

			</table>
		</body>
	</html>'''

cur.close()
