
userCal = float(input("Whats your calories requirements?"))
userPro = float(input("Whats your protein requirements?"))
userCarb = float(input("Whats your fat requirements?"))
userFat = float(input("Whats your carb requirements?"))

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
for z in range(0,20):
    for y in range(0,20):
        for x in range(0,20):
            print("%.1f" % one, "%.1f" % two, "%.1f" % three)
            print((one * steakCal) + (two * fishCal) + (three * potatoCal))
            print((one * steakPro) + (two * fishPro) + (three * potatoPro))
            print((one * steakCarbs) + (two * fishCarbs) + (three * potatoCarbs))
            print((one * steakFat) + (two * fishFat) + (three * potatoFat))
            three = three + 0.1
            if three > 2.1:
                two = two + 0.1
                three = three - 2.0
            if two > 2.1 :
                one = one + 0.1
                two = two - 2.0

'''
ok lets start with practise values. then we can make the calculation
lets start with creating 20 variables then we can make it so there are less. later.

next part is to work out the difference between the requirements and the calculation
then to be able to add them to an array and insertion sort it in order so the smallest difference is at the top
then after you have it working, make it so it works with any amounts of foods and any details
then make it more efficent - multi threaded programming
'''
