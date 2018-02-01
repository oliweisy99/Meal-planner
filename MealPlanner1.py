


userCal = float(input("Whats your calories requirements?"))
userPro = float(input("Whats your protein requirements?"))
userCarb = float(input("Whats your fat requirements?"))
userFat = float(input("Whats your carb requirements?"))

class chicken:
    def __init__(self):
        self.grams = 100
        self.calories = 150
        self.protein = 30
        self.fat = 15
        self.carbs = 20

class steak:
    def __init__(self):
        self.grams = 100
        self.calories = 125
        self.protein = 35
        self.fat = 20
        self.carbs = 25


class salad:
    def __init__(self):
        self.grams = 100
        self.calories = 110
        self.protein = 5
        self.fat = 5
        self.carbs = 20



one = 0.1
two = 0.1
three = 0.1
for z in range(0,20):
    for y in range(0,20):
        for x in range(0,20):
            print("%.1f" % one, "%.1f" % two, "%.1f" % three)
            three = three + 0.1
            if three > 2.1:
                two = two + 0.1
                three = three - 2.0
            if two > 2.1 :
                one = one + 0.1
                two = two - 2.0

'''
ok lets start with practise values. then we can make the calculation
next part is to work out the difference between the requirements and the calculation
then to be able to add them to an array and insertion sort it in order so the smallest difference is at the top
then after you have it working, make it so it works with any amounts of foods and any details
then make it more efficent - multi threaded programming
'''
