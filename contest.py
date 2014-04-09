import MySQLdb

class DbConnect:
	def __init__(self):
		self.con=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',db='bndwidth',)

	def execute(self, query):
		self.cursor = self.con.cursor()
		self.cursor.execute(query)
		self.con.commit()
		self.cursor.close()
		return True

	def lastrowid(self):
		return self.cursor.lastrowid
