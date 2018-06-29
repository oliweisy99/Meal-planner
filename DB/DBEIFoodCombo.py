import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook("/Users/OliverWeisfeld/Desktop/code/FoodDetails.xls")
sheet = book.sheet_by_name("FoodCombos")

# Establish a MySQL connection
database = pymysql.connect("localhost","testuser","test123","TESTDB" )

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    food = sheet.cell(r,0).value
    comboOne = sheet.cell(r,1).value
    comboTwo = sheet.cell(r,2).value
    comboThree = sheet.cell(r,3).value
    comboFour = sheet.cell(r,4).value
    comboFive = sheet.cell(r, 5).value

    sql = "INSERT INTO FOODCOMBOS(FOOD, COMBO1, \
           COMBO2, COMBO3, COMBO4, COMBO5) \
           VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % \
          (food, comboOne, comboTwo, comboThree, comboFour, comboFive)

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

