import pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS MEALS")

# Create table as per requirement
sql = """CREATE TABLE MEALS (
         CERL  CHAR(4),
         SWCH CHAR(4),
         MDSH CHAR(4),
         FDSH CHAR(4),
         TOST CHAR(4),
         SOUP CHAR(4),
         SALD CHAR(4),
         FBWL CHAR(4),
         MNTS CHAR(4),
         MVEG CHAR(4),
         MFRT CHAR(4),
         DFRT CHAR(4))"""

cursor.execute(sql)

# disconnect from server
db.close()