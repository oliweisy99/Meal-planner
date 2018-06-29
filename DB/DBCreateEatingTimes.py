import pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EATINGTIMES")

# Create table as per requirement
sql = """CREATE TABLE EATINGTIMES (
         BREK  CHAR(4),
         LNCH CHAR(4),
         DINR  CHAR(4),
         SNCK CHAR(4))"""

cursor.execute(sql)

# disconnect from server
db.close()