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
    name = sheet.cell(r,0).value
    grams = sheet.cell(r,1).value
    cals = sheet.cell(r,2).value
    pros = sheet.cell(r,3).value
    carbs = sheet.cell(r,4).value
    fats = sheet.cell(r, 5).value

    sql = "INSERT INTO FOOD(NAME, GRAMS, \
           CALS, PROS, CARBS, FATS) \
           VALUES ('%s', '%d', '%d', '%d', '%d', '%d' )" % \
          (name, grams, cals, pros, carbs, fats)

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        database.commit()
    except:
        # Rollback in case there is any error
        database.rollback()

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("I just imported ", columns, " columns and ", rows," rows to MySQL!")
