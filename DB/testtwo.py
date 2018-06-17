import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook("/Users/OliverWeisfeld/Desktop/code/Practise1.xls")
sheet = book.sheet_by_name("Practise1")

# Establish a MySQL connection
database = pymysql.connect("localhost","testuser","test123","TESTDB" )

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()


# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    firstName = sheet.cell(r,0).value
    lastName = sheet.cell(r,1).value
    age	= sheet.cell(r,2).value
    sex	= sheet.cell(r,3).value
    income	= sheet.cell(r,4).value

    sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
           LAST_NAME, AGE, SEX, INCOME) \
           VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
          (firstName, lastName, age, sex, income)
    # %s means string, %d means digit, %c means character

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        database.commit()
    except:
        # Rollback in case there is any error
        print("penis")
        database.rollback()

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print("")
print("All Done! Bye, for now.")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("I just imported ", columns, " columns and ", rows," rows to MySQL!")
