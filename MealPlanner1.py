
class user():
    userName = input("whats your name?")
    calories = float(input("Whats your calories requirements?"))
    protein = float(input("Whats your protein requirements?"))
    carbs = float(input("Whats your carbs requirements?"))
    fat = float(input("Whats your fat requirements?"))


class chicken():
    grams = 100
    calories = 31
    fat = 10
    carbs = 10
    protein = 10

class salad():
    grams = 100
    calories = 75
    fat = 5
    carbs = 30
    protein = 15

user()

# calculates how much grams of chicken you need to match your requirements of calories for it to 3 decimal places
def calc():
        if user.calories == chicken.calories:
            print("test success")
        else:
            holder = user.calories / chicken.calories
            amount = holder * chicken.grams
            print("%.3f" % amount, " grams of chicken for ", user.calories, " required calories")
