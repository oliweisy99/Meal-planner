#!/usr/bin/python

import pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
#sql = """INSERT INTO EMPLOYEE
 #               (FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)
  #  VALUES      ('Mac', 'Mohan', 20, 'M', 2000)"""

test = "penis"
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       (test, 'awesome', 4, 'F', 1000)
# %s means string, %d means digit, %c means character

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()