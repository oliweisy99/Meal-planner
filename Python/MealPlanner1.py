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
        self.tags = [" " for i in range(0,15)]
      # self.price = 0

# variables for text file assignments
foodList = [0] * 50
index = 0
n = 48
i = 1
x = 0
z = 0
nom = None
tester = None
count = 0
colonCount = 0
end = False
nm = None
check = None
fo = open("Foods", "r+")
fo.seek(n, 0)
incre = 0
bool = True

# text file assignment to class function
def assign(coCnt):
    global count, check, end, nom, colonCount, n, index, list, x, bool, z, tester
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
        x = 0
        fo.seek((n - (count - 1))) # read from first letter
        tester = fo.read(4)
        print(tester)
        #foodList[index].tags[z] = str(fo.read(4))
        x = x + 4
        fo.seek((n - (count - 1)) + x)  # starts from ',' or ']'
        while bool == True:
            if fo.read(1) == ",":
                fo.seek((n - (count - 1)) + (x+1)) # read from first letter after ','
                z = z + 1
                tester = fo.read(4)
                print(tester)
                print("tell", fo.tell())
                #foodList[index].tags[z] = str(fo.read(4))
                x = x + 5
                print("x=",x)
                print("count=", count)
                print("n=", n)
                fo.seek((n - (count - 1)) + x)
                print("tell", fo.tell())
            if fo.read(1) == "]":
                print("test")
                x = 0
                z = 0
                fo.seek(n+1)
                bool = False
                break
        bool = True
    if coCnt == 8:
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
    print("check=", check)
    fo.seek(n + 1, 0)
    print("CoCnt=", colonCount)
    assign(colonCount)


fo.close()

userCal = float(input("Whats your calories requirements?"))
userPro = float(input("Whats your protein requirements?"))
userCarb = float(input("Whats your carb requirements?"))
userFat = float(input("Whats your fat requirements?"))

tempList = [0] * 5 # used to find smallest value for mulitiList
multiList = [0] * 50 # multiplier list for each food
X = [[0.00 for i in range(10)] for j in range(10)]
i = 0
n = 0
for i in range(0,4): # the number 3 needs to be a variable which will be determined based on the meal being created
# but for now just to test, it remains 3 as there are 3 test foods

    tempList[1] = float(userCal / int(foodList[i].cals))
    tempList[2] = float(userPro / int(foodList[i].pros))
    tempList[3] = float(userCarb / int(foodList[i].carbs))
    tempList[4] = float(userFat / int(foodList[i].fats))

# insertion sort:
    for index in range(len(tempList)): # to go through each value in the array
        insertItem = tempList[index] # stores value which gets replaced
        currentitem = index - 1
        while tempList[currentitem] > insertItem and currentitem > 0: # going through individual value compared to other values
            tempList[currentitem + 1] = tempList[currentitem]
            currentitem = currentitem - 1
        tempList[currentitem + 1] = insertItem

    multiList[i] = float(tempList[1])
    X[n][i] = multiList[i] * float(foodList[i].cals)
    X[n+1][i] = multiList[i] * float(foodList[i].pros)
    X[n+2][i] = multiList[i] * float(foodList[i].carbs)
    X[n+3][i] = multiList[i] * float(foodList[i].fats)


'''
print(X[0][0]) ~ first food + cals
print(X[1][0]) ~ pros
print(X[2][0]) ~ carbs
print(X[3][0]) ~ fats
print(X[0][1]) ~ next food + cals
'''

for i in range(0,4):
    print(multiList[i])

class number:
    def __init__(self):
        self.on = 0
        self.tw = 0
        self.thre = 0
        self.fur = 0

myList = [number() for index in range(0,7)]

one = 0.1
two = 0.1
three = 0.1
four = 0.1
holder = None
count = 0
orderArr = [0, 1000, 1000, 1000, 1000, 1000]
for w in range(0,20):
    for z in range(0,20):
        for y in range(0,20):
            for x in range(0,20):

                # working out difference
                calDif = userCal - ((one * X[0][0]) + (two * X[0][1]) + (three * X[0][2])) + (four * X[0][3])
                proDif = userPro - ((one * X[1][0]) + (two * X[1][1]) + (three * X[1][2])) + (four * X[1][3])
                carbDif = userCarb - ((one * X[2][0]) + (two * X[2][1]) + (three * X[2][2])) + (four * X[2][3])
                fatDif = userFat - ((one * X[3][0]) + (two * X[3][1]) + (three * X[3][2])) + (four * X[3][3])
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
                myList[count].fur = four
                count = 0

                # moving up numbers
                four = four + 0.1
                if four > 2.1:
                    three = three + 0.1
                    four = four - 2.0
                if three > 2.1:
                    two = two + 0.1
                    three = three - 2.0
                if two > 2.1 :
                    one = one + 0.1
                    two = two - 2.0

for index in range(1,6):
    print("%.2f" % orderArr[index], " : ","%.1f" %  myList[index].on, " : ", "%.1f" % myList[index].tw, " : ", "%.1f" % myList[index].thre, " : ", "%.1f" % myList[index].fur)

'''

all this is initially for yourself, then when you have it working the way you want, start adding customers

Research into:
- making high quality meals 
- multithreading for faster programming
'''

