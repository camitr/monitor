#!/usr/bin/python
import cgi
print '''Content-type:text/html\n'''

print'''<html>


	<head>
		<title>Bandwidth Test</title>
	</head>
	
	<body>
		<form action="TestData.py" method="post">
			Test ID: 	   <input type="text" name="ID"><br>
			Number of Machine: <input type="text" name="total_machine"><br>
			<table border=0>
				<tr>
					<td>
					

						<input type="checkbox" name="os1" value="L1" checked onclick=enable(this.checked,'ifm1')>Linux 1<br>
					</td>	
					<td>

						<input type="checkbox" name="live" value="c1" checked onclick=enable(this.checked,'ifm5')>Live all <br>
				</tr>
				<tr>
					<td>

						<input type="checkbox" name="os2" value="L2" checked onclick=enable(this.checked,'ifm2')>Linux 2<br> 
					</td>
				</tr>
				<tr>
					<td>
						<input type="checkbox" name="os3" value="X1" checked onclick=enable(this.checked,'ifm3')>XP 1<br>		
					</td>

				</tr>
				<tr>
					<td>
							
						<input type="checkbox" name="os4" value="X2" checked onclick=enable(this.checked,'ifm4')>XP 2<br>	
					</td>
					</tr>
			
			</table>

			<table width=100%>
				<tr>
					<td>
						<iframe id='ifm1' style='display:none' src=http://10.129.200.50/cgi-bin/monitor/L1Run.py  width=100% height=100% ></iframe>

					</td>
					<td>
					</td>
				</tr>
				<tr>
					<td>
						<iframe id='ifm3' style='display:none' src=http://10.129.200.50/cgi-bin/monitor/XpRun.py  width=100% height=100% ></iframe>
					</td>
					<td>
					<!--	<iframe id='ifm4' style='display:none' src=http://10.129.200.50/cgi-bin/monitor/ShwDataXp.py  width=100% height=100% ></iframe>-->
					</td>
				</tr>
				<tr>
					<td>
						<iframe id='ifm5' style='display:none' src=http://10.129.200.50/cgi-bin/monitor/LiveBand.py  width=100% height=100% ></iframe>
					</td>
				</tr>
			</table>


			<script language='JavaScript'>
				function enable(isEnable,os){
					if (isEnable==false)
						document.getElementById(os).style.display='none';
					else
						document.getElementById(os).style.display='inline';

								}
			</script>	

		</form>

	</html>'''






