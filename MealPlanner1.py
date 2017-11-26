
class user():
    userName = input("whats your name?")
    calories = float(input("Whats your calories requirements?"))
    protein = float(input("Whats your protein requirements?"))
    carbs = float(input("Whats your carbs requirements?"))
    fat = float(input("Whats your fat requirements?"))


class chicken():
    grams = 82
    calories = 31
    fat = 10
    carbs = 10
    protein = 10

class steak():
    grams = 100
    calories = 10
    fat = 10
    carbs = 10
    protein = 10

class salad():
    grams = 100
    calories = 10
    fat = 10
    carbs = 10
    protein = 10

class potato():
    grams = 100
    calories = 10
    fat = 10
    carbs = 10
    protein = 10

class fish():
    grams = 100
    calories = 10
    fat = 10
    protein = 10
    carbs = 10

user()

if user.calories == chicken.calories :
    print("test success")
else :
    holder = user.calories / chicken.calories
    amount = holder * chicken.grams
    print(amount, " grams of chicken for ", user.calories, " required calories")
#  calculates how much grams of chicken you need to match your requirements of calories for it

# next stage is to work out how much protein, fat and carbs you need from the chicken
# then after that you work out with calories and put it all together
# then after that, you did it across multiple foods