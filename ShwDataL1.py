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
import MySQLdb as mdb

form = cgi.FieldStorage()
keyword = form.getvalue('keyword')


print '''
		 <body>

			<h2> Packet size and Upload & Download Bandwidth of Clients:Kbps</h2>
			<iframe src=http://10.129.200.50/cgi-bin/monitor/shwband.py  width=100% height=50% ></iframe>

			<h2> Percentage of Packet size Upload by client</h2>
			<iframe src=http://10.129.200.50/cgi-bin/monitor/shwpckt.py  width=100% height=30% ></iframe>
			
			<h2> Percentage of Packet size  by Server</h2>
			<iframe src=http://10.129.200.50/cgi-bin/monitor/ShwPcktDwn.py  width=100% height=30% ></iframe>


			<table border=1 width=100% bgcolor=#6666CC>
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


			</table>
		</body>
	</html>'''


