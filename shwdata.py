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
cgitb.enable()
import MySQLdb as mdb

form = cgi.FieldStorage()
keyword = form.getvalue('keyword')


#print "<meta http-equiv=refresh content=2>"
print '''
		 <body>

			<h2> Packet size and Upload & Download Bandwidth of Clients</h2>
			<iframe src=http://10.129.200.50/cgi-bin/monitor/shwband.py  width=100% height=50% ></iframe>

			<h2> Percentage of different packets size capture</h2>
			<iframe src=http://10.129.200.50/cgi-bin/monitor/shwpckt.py  width=100% height=30% ></iframe>

			<table border=0 width=100% bgcolor=#6666CC>
				<form action=/cgi-bin/monitor/run-linux.py method=post/>
				<tr>
					<td>

						<button type=submit autofocus style='width=48;height=60;background-color:#D2B48C'>Linux</button>
				</form>
					</td>

				<form action=/cgi-bin/monitor/kill.sh method=post/>
					<td>

						<button type=submit autofocus style='width=48;height=60;background-color:#D2B48C'>kill-linux</button>
					 </td>
				</form>

				<form action=/cgi-bin/monitor/sshpython.py method=post/>
					<td>
						<button type=submit autofocus style='width=48;height=60;background-color:#98FB98'> XP2</button>
				</form>
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

