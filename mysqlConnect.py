import csv
import MySQLdb
import datetime

#connection = MySQLdb.connect("10.129.200.80","root","123","bndwidth")
#cursor = connection.cursor()
#cursor.execute("SELECT VERSION()")
#data=cursor.fetchone()
#print "Database version: %s" % data

#connection.close()
#print datetime.datetime.utcnow()
conn=MySQLdb.connect(host='10.129.200.50',user='root',passwd='123',db='bndwidth',local_infile=1)

cursor=conn.cursor()

query= """ LOAD DATA LOCAL INFILE 'TestAnalysis.csv' INTO TABLE Analysis FIELDS TERMINATED BY ',' """
query2=""" LOAD DATA LOCAL INFILE 'Percentage.csv' INTO TABLE Packet_Percent FIELDS TERMINATED BY ',' """
#print query
#
print "connection Done"

cursor.execute(query)

cursor.execute(query2)
#
conn.commit()
cursor.close()
#
