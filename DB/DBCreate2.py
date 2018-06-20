import pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS TAGS")

# Create table as per requirement
sql = """CREATE TABLE TAGS (
         BREK  CHAR(8),
         LNCH  CHAR(8),
         DINR  CHAR(8),
         SNCK CHAR(8),
         VEGY CHAR(8),
         MEAT CHAR(8))"""

cursor.execute(sql)

# disconnect from server
db.close()