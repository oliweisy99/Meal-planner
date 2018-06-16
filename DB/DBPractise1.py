import pymysql

f = open(r"Practise1.csv","r") #to get to csv format, convert to sv format, then read excel file as textfile, then c&p
fString = f.read()

#conver string to list
fList = []
for line in fString.split('\n'):
    fList.append(line.split(','))

print(fList[0][4])

#open connection to database
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB") #might have to change test123 to other password

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exists using execute() method
cursor.execute("DROP TABLE IF EXISTS STUDENTS")

# Create column names from the first line in fList
FIRST_NAME = fList[0][0]; LAST_NAME = fList[0][1]; AGE = fList[0][2]; GENDER = fList[0][3]; DEGREE = fList[0][4]

# Create STUDENT table // place a comma after each new column except the last
queryCreateStudentTable = """CREATE TABLE STUDENTS(
                            varchar(255) no null,
                            varchar(255) no null,
                            int,
                            char(1),
                            char(2)
                            )""".format(FIRST_NAME, LAST_NAME, AGE, GENDER, DEGREE)

cursor.execute(queryCreateStudentTable)

db.close()

'''
not currently working, but i think there is a better way of doing it. maybe with panda, or something.
need to be able to read excel data, then transfer it into database format.
'''