import pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS FOODCOMBOS")

# Create table as per requirement
sql = """CREATE TABLE FOODCOMBOS (
         FOOD  CHAR(4),
         COMBO1 CHAR(8),
         COMBO2  CHAR(8),
         COMBO3 CHAR(8),
         COMBO4 CHAR(8),
         COMBO5 CHAR(8))"""

cursor.execute(sql)

# disconnect from server
db.close()