import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook("/Users/OliverWeisfeld/Desktop/code/Tags.xls")
sheet = book.sheet_by_name("Sheet1")

# Establish a MySQL connection
database = pymysql.connect("localhost","testuser","test123","TESTDB" )

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    breakfast = sheet.cell(r,0).value
    lunch = sheet.cell(r,1).value
    dinner = sheet.cell(r,2).value
    primary = sheet.cell(r,3).value
    side = sheet.cell(r,4).value
    highCarbs = sheet.cell(r, 5).value
    highPros = sheet.cell(r,6).value
    highFat = sheet.cell(r, 7).value
    lowCarb = sheet.cell(r, 8).value
    vegetarian = sheet.cell(r, 9).value

    sql = "INSERT INTO TAGS(BREK, LNCH, \
           DINR, PRIM, SIDE, HCRB, HPRO, HFAT, LCRB, VEGY) \
           VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s' )" % \
          (breakfast, lunch, dinner, primary, side, highCarbs, highPros, highFat, lowCarb, vegetarian)

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        database.commit()

    except:
        # Rollback in case there is any error
        database.rollback()
        print("Error, try again")

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("I just imported ", columns, " columns and ", rows, " rows to MySQL!")

