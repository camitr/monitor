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
			<table border=0 width=100% height=50% cellspacing=0 >
				<tr>
					<td><b>XP Client Bandwidth</b>
					<!--	<h2>Upload & Download Bandwidth of XP Clients:Kbps</h2>-->
					<iframe src=http://10.129.200.50/cgi-bin/monitor/ShwDataXp.py  width=100% height=100% ></iframe>
					</td>
					<td><b>Live Bandwidth</b>

					<!--	<h2> Packet size and Upload & Download Bandwidth of Clients:Kbps</h2>-->
						<iframe align='right'src=http://10.129.200.50/cgi-bin/monitor/shwband.py  width=100% height=100% ></iframe>

					</td>
				</tr>
				<tr>
					<td><b> Linux Client Bandwidth
	
						<iframe src=http://10.129.200.50/cgi-bin/monitor/ShwBandL1.py  width=100% height=100% ></iframe>
					</td>
					<td><b>Live Download Packet Percent</b>
						<!--<h2> Percentage of Packet size  by Server</h2>-->
						<iframe src=http://10.129.200.50/cgi-bin/monitor/ShwPcktDwn.py  width=100% height=100% ></iframe>
					</td>
				</tr>
				<tr>
					<td>
					</td>
					<td><b>Live Upload Packet Percent</b>
					<!--	<h2> Percentage of Packet size Upload by client</h2>-->
						<iframe src=http://10.129.200.50/cgi-bin/monitor/shwpckt.py  width=100% height=100% ></iframe>
					</td>
				</tr>
			</table>
	
			<table border=1 width=50% height=30% bgcolor=#6666CC>
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
				<tr>
				<form action=/cgi-bin/monitor/delall.py method=post/>
					<td colspan=4>
				<!--		<div style="text-align:center">-->
						<button type=submit autofocus style='width:48;height:60;background-color:#FF5353;margin-left:50%'>Delete</button>
					<!--	</div>-->
					</td>
				</tr>
				</form>

			</table>
		</body>
	</html>'''


