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
         PRIM  CHAR(8),
         SIDE  CHAR(8),
         HCRB  CHAR(8),
         HPRO  CHAR(8),
         HFAT  CHAR(8),
         LCRB  CHAR(8),
         VEGY CHAR(8))"""

cursor.execute(sql)

# disconnect from server
db.close()