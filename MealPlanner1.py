#nom.com
#naughty
#ominpresent
#meals

userCal = float(input("Whats your calories requirements?"))
userPro = float(input("Whats your protein requirements?"))
userCarb = float(input("Whats your carb requirements?"))
userFat = float(input("Whats your fat requirements?"))

'''
index = 2
count = 1
myArray = [0, 1, 2, 3, 4, 5]

for count in range(0,5):
    item = int(input("what is your input?"))
    myArray[count + 1] = item
# takes input and stores input into array

when array is full, then start seeing if the totaldif is smaller than the first item of the array
to check if array is full, the values in array are bigger than 0 as array starts with 'none' values
use a boolean to check if all values are greater than 0, and if boolean is true, then it skips 
the code of adding in and just moves to the comparison side 
if totaldif value is not smaller than first value, then move on in the loop
if it is, add it to the insertion sort to see if it moves up: using while loop


for index in range(index, len(myArray)):
    insertItem = myArray[index]
    currentitem = index - 1
    while myArray[currentitem] > insertItem and currentitem > 0:
        myArray[currentitem + 1] = myArray[currentitem]
        currentitem = currentitem - 1
    myArray[currentitem + 1] = insertItem
# goes through each number in the array and loops until the number is smaller than the one in front
# switches the number round if the count number is bigger than the number after it in the array
# move along the array if the number is smaller and ends the while loop of switching numbers

print(myArray)
'''


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

one = 0.1
two = 0.1
three = 0.1
holder = None
orderArr = [0, 1000, 1000, 1000, 1000, 1000]

for z in range(0,20):
    for y in range(0,20):
        for x in range(0,20):
            # print("%.1f" % one, "%.1f" % two, "%.1f" % three)
            # working out difference
            calDif = userCal - ((one * steakCal) + (two * fishCal) + (three * potatoCal))
            proDif = userPro - ((one * steakPro) + (two * fishPro) + (three * potatoPro))
            carbDif = userCarb - ((one * steakCarbs) + (two * fishCarbs) + (three * potatoCarbs))
            fatDif = userFat - ((one * steakFat) + (two * fishFat) + (three * potatoFat))
            totalDif = abs(calDif) + abs(proDif) + abs(carbDif) + abs(fatDif)
            # print(totalDif)
            if y == 0.1 and x < 6:
                orderArr[x] = totalDif
            if orderArr[0] > totalDif :
                orderArr[0] = totalDif
            for index in range(1,6):
                if orderArr[index] > totalDif:
                    holder = orderArr[index]
                    orderArr[index] = totalDif
                    orderArr[index - 1] = holder
            three = three + 0.1
            if three > 2.1:
                two = two + 0.1
                three = three - 2.0
            if two > 2.1 :
                one = one + 0.1
                two = two - 2.0

for index in range(0,6):
    print("%.2f" % orderArr[index])
'''
- add to an array using insertion sort to get the closest value and so you dont have to sort through all posibilites
- make sure it works with multiple amounts of foods to create actual meals and make sure maths works 
- make the code better and more accurate to get results faster: 
procedures, multi threading, 0.001, using less variables, making code more efficient, cutting down calculations etc.

once you have the code to generate the best variations, now you can start making meals best on requriements 
then you can start adding features or start making it into a website 
then you start adding more features and get the business side of it sorted
'''

