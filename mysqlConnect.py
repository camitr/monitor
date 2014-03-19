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


query1= """ LOAD DATA LOCAL INFILE 'TestAnalysis.csv' INTO TABLE Analysis FIELDS TERMINATED BY ',' """
#var="select max(id)  from Analysis where machine='apple'"

cursor.execute(query1)
#cursor.execute(var)
#result=cursor.fetchone()[0]

#cursor.execute("insert into Packet_Percent (id) values('result')")
#cursor.execute(insert)
##query2=""" LOAD DATA LOCAL INFILE 'Pecentage.csv' INTO TABLE Packet_Percent FIELDS TERMINATED BY ',' """
query2=""" LOAD DATA LOCAL INFILE 'Pecentage.csv' INTO TABLE Packet_Percent_Client FIELDS TERMINATED BY ',' """
cursor.execute(query2)

query3=""" LOAD DATA LOCAL INFILE 'PecentageDwn.csv' INTO TABLE Packet_Percent_Server FIELDS TERMINATED BY ',' """
cursor.execute(query3)
#print query
#
print "connection Done"


#print "Maxid=",result

#
conn.commit()
cursor.close()
#
