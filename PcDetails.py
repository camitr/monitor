#!/usr/bin/python

import cgi,cgitb
cgitb.enable()

print'''Content-type: text/html\n'''

print'''<DOCTYPE html> 
	<html><head>
			<meta charset="utf-8">
			<title>PC Details</title>
		</head>

			<body>
				<form action="PcData.py" method=post>
				<div align="center">
				<H1><b>Add Test PC Details</H1></b>
				</div>
				<table border=0 align="center">
					<tr>
						<td>
							<div align="right">
							<b>PC Name:</b><input type="text" name="PC" size="30" value="" required>
							</div>
						</td>
						<td>
							<div align="right">
							<b>User:</b><input type="text" name="user" size="30" value="" >	
							</div>
						</tb>
					</tr>
					<tr>
						<td>
							<div align="right">
						<b>IP:</b><input type="text" name="IP"  pattern="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" size="30" value="" >
							</div>
						</td>
						<td>
							<div align="right">
							<b>Password:</b><input type="password" name="Password" size="30" value"">							
							</div>
						</td>				
				
					</tr>
					<tr>
						<td>
							<div align="right">
							<b>OS:</b><input type="text" name="OS" size="30" value="" >
							</div>
						</td>
					</tr>
					<tr>
						<td>
						</td>
						<td>
							<div align="right">
							<input type="submit" name="submit" size="25" value="submit">	
							</div>
						</td>
					</tr>
				</table>
				</form>
			</body>
	</html>'''
