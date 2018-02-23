userCal = float(input("Whats your calories requirements?"))
userPro = float(input("Whats your protein requirements?"))
userCarb = float(input("Whats your carb requirements?"))
userFat = float(input("Whats your fat requirements?"))


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

class number:
    def __init__(self):
        self.one = 0
        self.two = 0
        self.three = 0
        self.difference = 0

myList = [number() for index in range(0,5)]
myList[0].one = 2
myList[0].two = 4
myList[0].three = 5



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

            '''
            if myList[0].difference > totaldif:
                holder = ml.d[index]
                ml.d[index] = totalDif
                ml.d[index - 1] = holder
                mylist[index].one = one
                mylist[index].two = two
                mylist[index].three = three
            '''
            # sorting array thing
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
- make sure maths works with more than 3 foods
- make the code better and more accurate to get results faster: 
procedures, multi threading, 0.001, using less variables, making code more efficient, cutting down calculations etc.
- make sure it works with multiple amounts of foods to create actual meals, so have lots of foods and 
make 3 different meals based on the foods to get really close amounts. 

start making good meals based on variations and categories etc so all is needed is just switching of foods into 
different meals - sandwiches, salads, meat meals, cereals etc.
once you have the code to generate the best variations, now you can start making meals best on requirements such as 
price, needs, aims and start adding in foods from websites to get it done. 
then you can start adding more features or start making it into a website 
then you start getting the business side of it sorted so it can be shopped, made and delivered
'''

