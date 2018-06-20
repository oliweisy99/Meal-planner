#!/usr/bin/python

import pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS FOOD")

# Create table as per requirement
sql = """CREATE TABLE FOOD (
         NAME  CHAR(20) NOT NULL,
         GRAMS  INT NOT NULL,
         CALS INT NOT NULL,  
         PROS INT NOT NULL,
         CARBS INT NOT NULL, 
         FATS INT NOT NULL,
         PRICE FLOAT NOT NULL,
         ID CHAR(8) NOT NULL)"""

cursor.execute(sql)

# disconnect from server
db.close()