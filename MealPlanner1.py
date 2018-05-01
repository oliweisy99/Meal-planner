#MEAL PLANNER

# food super class
class food:
    def __init__(self):
        self.name = ""
        self.grams = 0
        self.cals = 0
        self.pros = 0
        self.carbs = 0
        self.fats = 0
      # self.attributes = []

# variables for text file assignments
foodList = [0] * 50
index = 0
n = 41
i = 1
nom = None
count = 0
colonCount = 0
end = False
nm = None
check = None
fo = open("Foods", "r+")
fo.seek(n, 0)

# text file assignment to class function
def assign(coCnt):
    global count, check, nm, end, nom, colonCount, n, index, list
    if isinstance(check, str) == True :
        nom = str(check)
    else:
        nom = int(check)
    if coCnt == 1:
        if check == "#":
            end = True
        else:
            foodList[index] = food()
            foodList[index].name = nom
    if coCnt == 2:
        foodList[index].grams = nom
    if coCnt == 3:
        foodList[index].cals = nom
    if coCnt == 4:
        foodList[index].pros = nom
    if coCnt == 5:
        foodList[index].carbs = nom
    if coCnt == 6:
        foodList[index].fats = nom
    if coCnt == 7:
        colonCount = 0
        n = n - count
        index = index + 1
    count = -1
    check = fo.read(i)

# text file reader loop
while end == False:
    while check != ":" or check == "#":
        check = fo.read(i)
        if check == ":" or check == "#":
            colonCount = colonCount + 1
            break
        if check != ":" and check != "#":
            n = n + 1
            count = count + 1
            fo.seek(n,0)
    fo.seek(n - count, 0)
    check = fo.read(count)
    fo.seek(n + 1, 0)
    assign(colonCount)

fo.close()

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

tempList = [0] * 5 # used to find smallest value for mulitiList
multiList = [0] * 50 # multiplier list for each food
X = [[0 for i in range(10)] for j in range(10)]

i = 0
tempList[1] = float(userCal / int(foodList[i].cals))
tempList[2] = float(userPro / int(foodList[i].pros))
tempList[3] = float(userCarb / int(foodList[i].carbs))
tempList[4] = float(userFat / int(foodList[i].fats))

for index in range(len(tempList)): # to go through each value in the array
    insertItem = tempList[index] # stores value which gets replaced
    currentitem = index - 1
    while tempList[currentitem] > insertItem and currentitem > 0: # going through individual value compared to other values
        tempList[currentitem + 1] = tempList[currentitem]
        currentitem = currentitem - 1
    tempList[currentitem + 1] = insertItem

multiList[i] = tempList[1]

'''
we are going to need to calculate the smallest multiplier for each food
with the users inputs

might have to have multiple lists or a class with two different lists in it
whatever is easier

Test[0] = userCal / foodList[i].cals
test[1] = userPro / foodList[i].pros
test[2] = usercarb / foodList[i].carbs
test[3] = userfat / foodList[i].fats

then take smallest value from those, and put it into new array
multipliers[i] the smallest value from test[] and i represents the food number as well from foodList[i]
could rearrange it then assign smallest to mulitplier[i]

so now we have the multiplier, for each food.
now there is the other things we need to work out 
which is the food cals/pros etc. * food multiplier
could use a 2d array and each row is the food. 
and run everything through a loop when letters get incremented until something. 
X[n][i] = multiplier[i] * foodList[i].cals
X[n][i] = multiplier[i] * foodList[i].pros
X[n][i] = multiplier[i] * foodList[i].carbs
X[n][i] = multiplier[i] * foodList[i].fats
where n is being looped for the next food as well so it can go in the next column
the X 2d array contains the digits which get multiplied and added with the ratios


'''

steakMulti = userFat / steak().fat #4.6
fishMulti = userPro / fish().protein #4.625
potatoMulti = userCarb / potato().carbs #9.266667

# these aren't the values calculated, they are just selected from previously done calculations

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

we could just have lists for each one have the lists are part of classes
as each one can be repeated. just need the multiplier. 

Next thing to do is to get all food from classes, using excel spreadsheet maths
and then create the meals. 

once we have the all the information stored like it is above, then
we can start adding in more foods, making smarter meals etc. 

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
all this is initially for yourself, then when you have it working the way you want, start adding customers

- make sure maths works with more than 3 foods

- make the code better and more accurate to get results faster: 
procedures, multi threading, 0.001, using less variables, making code more efficient, cutting down calculations etc.
it needs to be quick if you want to create loads of different unique meals for a week, and in the future for a month 
and also to be able to completely create and calculate a new meal plan if and when the user changes foods 

- make sure it works with multiple amounts of foods to create actual meals, so have lots of foods and 
make 3 different meals based on the foods to get really close amounts. 

- have it so it displays the amount of each food that is needed to get close to requirements
# we can have variables for each food [PRIM, MEAT, SOIL, TAST, SIDE, SUCE ETC.]
# PRIM = primary food, made for dinners / main courses 
# SIDE = side dish that go with PRIMs

start making good meals based on variations and categories etc so all is needed is just switching of foods into 
different meals - sandwiches, salads, meat meals, cereals etc.
do research into making good meals, types of meals etc.
once you have the code to generate the best variations, now you can start making meals based on requirements such as 
price, needs, aims and start adding in foods from websites to get it done. 
then you can start adding more features whilst learning website development 
then you start getting the business side of it sorted so meals can be shopped, made and delivered
'''

