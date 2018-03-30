class food:
    def __init__(self):
        self.name = ""
        self.grams = 0
        self.cals = 0
        self.pros = 0
        self.carbs = 0
        self.fats = 0

'''
fo = open("Foods", "r+")
str = fo.read(40)
print(str)
position = fo.tell()
print("Current file position : ", position)
position = fo.seek(40, 0)
str = fo.read(22)
print("Again read String is :", str)
fo.close()
'''

n = 40
i = 1
count = 0
colonCount = 0
end = False
nm = ""
check = ""
fo = open("Foods", "r+")
fo.seek(n, 0)
while end == False:
    while check != ":":
        check = fo.read(i)
        if check == ":":
            colonCount = colonCount + 1
            break
        if check != ":":
            n = n + 1
            count = count + 1
            fo.seek(n,0)
    fo.seek(n-count, 0)
    check = fo.read(count)
    nm = str(check)
    check = food()
    check.name = nm
    if colonCount == 1:
        # you want it to read the next digits and assign it to grams
        print()
    fo.close()

'''

    check is now == steak
    check = food()
    check.name = str(check)    
    if check == ":":
        count += 1
    if count == 1:
    if count == 2:
    if count == 3:
    if count == 4:
    if count == 5:
        digit = food.fats
        colonCount = 0
        also moves down a line 
        
end is = True if the file reads #.
fo.close() afterwards. 

we want to be able to get information from file and then store it into food class

'''
userCal = float(input("Whats your calories requirements?"))
userPro = float(input("Whats your protein requirements?"))
userCarb = float(input("Whats your carb requirements?"))
userFat = float(input("Whats your fat requirements?"))

'''
add foods from text file to the class by reading from it and using name as the variable
https://www.tutorialspoint.com/python/python_files_io.htm 
all information needed about using files is in the link above


so what we want it to do is go through the file, and in a loop add it to the food class
we could store the name of the food in an array maybe so we could access it later. 
'''

steak = food()
steak.name = "steak"
steak.cals = 100
steak.carbs = 25
steak.grams = 100
steak.pros = 40
steak.fats = 20


class fish:
    def __init__(self):
        self.grams = 100
        self.calories = 125
        self.protein = 40
        self.fat = 10
        self.carbs = 20

class steak:
    def __init__(self):
        self.grams = 100
        self.calories = 150
        self.protein = 35
        self.fat = 15
        self.carbs = 25


class potato:
    def __init__(self):
        self.grams = 100
        self.calories = 90
        self.protein = 10
        self.fat = 5
        self.carbs = 30

steakMulti = userFat / steak().fat #4.6
fishMulti = userPro / fish().protein #4.625
potatoMulti = userCarb / potato().carbs #9.266667

steakCal = steak().calories * steakMulti
steakPro = steak().protein * steakMulti
steakCarbs = steak().carbs * steakMulti
steakFat = steak().fat * steakMulti

fishCal = fish().calories * fishMulti
fishPro = fish().protein * fishMulti
fishCarbs = fish().carbs * fishMulti
fishFat = fish().fat * fishMulti

potatoCal = potato().calories * potatoMulti
potatoPro = potato().protein * potatoMulti
potatoCarbs = potato().carbs * potatoMulti
potatoFat = potato().fat * potatoMulti

'''
sort this out to work with multiple foods
'''


class number:
    def __init__(self):
        self.on = 0
        self.tw = 0
        self.thre = 0

myList = [number() for index in range(0,7)]


one = 0.1
two = 0.1
three = 0.1
holder = None
count = 0
orderArr = [0, 1000, 1000, 1000, 1000, 1000]

for z in range(0,20):
    for y in range(0,20):
        for x in range(0,20):

            # working out difference
            calDif = userCal - ((one * steakCal) + (two * fishCal) + (three * potatoCal))
            proDif = userPro - ((one * steakPro) + (two * fishPro) + (three * potatoPro))
            carbDif = userCarb - ((one * steakCarbs) + (two * fishCarbs) + (three * potatoCarbs))
            fatDif = userFat - ((one * steakFat) + (two * fishFat) + (three * potatoFat))
            totalDif = abs(calDif) + abs(proDif) + abs(carbDif) + abs(fatDif)

            if y == 0.1 and x < 6:
                orderArr[x] = totalDif
            if orderArr[0] > totalDif :
                orderArr[0] = totalDif

            for index in range(1,6):
                if orderArr[index] > totalDif:
                    count += 1
                    holder = orderArr[index]
                    orderArr[index] = totalDif
                    orderArr[index - 1] = holder

            myList[count].on = one
            myList[count].tw = two
            myList[count].thre = three
            count = 0

            # moving up numbers
            three = three + 0.1
            if three > 2.1:
                two = two + 0.1
                three = three - 2.0
            if two > 2.1 :
                one = one + 0.1
                two = two - 2.0

for index in range(1,6):
    print("%.2f" % orderArr[index], " : ","%.1f" %  myList[index].on, " : ", "%.1f" % myList[index].tw, " : ", "%.1f" % myList[index].thre)
'''
- make sure maths works with more than 3 foods
- make the code better and more accurate to get results faster: 
procedures, multi threading, 0.001, using less variables, making code more efficient, cutting down calculations etc.
- make sure it works with multiple amounts of foods to create actual meals, so have lots of foods and 
make 3 different meals based on the foods to get really close amounts. 
have it so it displays the amount of each food that is needed to get close to requirements
# we can have variables for each food [PRIM, MEAT, SOIL, TAST, SIDE, SUCE ETC.]
# PRIM = primary food, made for dinners or main course 
# SIDE = side dish

start making good meals based on variations and categories etc so all is needed is just switching of foods into 
different meals - sandwiches, salads, meat meals, cereals etc.
do research into making good meals, types of meals etc.
once you have the code to generate the best variations, now you can start making meals best on requirements such as 
price, needs, aims and start adding in foods from websites to get it done. 
then you can start adding more features whilst learning website development 
then you start getting the business side of it sorted so meals can be shopped, made and delivered
'''

