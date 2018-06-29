import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook("/Users/OliverWeisfeld/Desktop/code/FoodDetails.xls")
sheet = book.sheet_by_name("Meals")

# Establish a MySQL connection
database = pymysql.connect("localhost","testuser","test123","TESTDB" )

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    cereal = sheet.cell(r,0).value
    sandwich = sheet.cell(r,1).value
    meatDish = sheet.cell(r,2).value
    fishDish = sheet.cell(r,3).value
    toast = sheet.cell(r,4).value
    soup = sheet.cell(r, 5).value
    salad = sheet.cell(r, 6).value
    fruitBowl = sheet.cell(r, 7).value
    mixedNuts = sheet.cell(r, 8).value
    mixedVegys = sheet.cell(r, 9).value
    mixedFruits = sheet.cell(r, 10).value
    driedFruits = sheet.cell(r, 11).value


    sql = "INSERT INTO MEALS(CERL, SWCH, \
           MDSH, FDSH, TOST, SOUP, SALD, FBWL, MNTS, MVEG, MFRT, DFRT) \
           VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
          (cereal, sandwich, meatDish, fishDish, toast, soup, salad, fruitBowl, mixedNuts, mixedVegys, mixedFruits, driedFruits)

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

