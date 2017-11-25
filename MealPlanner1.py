
class user():
    userName = input("whats your name?")
    calories = float(input("Whats your calories requirements?"))
    protein = float(input("Whats your protein requirements?"))
    carbs = float(input("Whats your carbs requirements?"))
    fat = float(input("Whats your fat requirements?"))


class chicken():
    calories = 10
    fat = 10
    carbs = 10
    protein = 10

class salad():
    calories = 10
    fat = 10
    carbs = 10
    protein = 10

class potato():
    calories = 10
    fat = 10
    carbs = 10
    protein = 10

class fish():
    calories = 10
    fat = 10
    protein = 10
    carbs = 10

user()

if user.calories == chicken.calories :
    print("test success")
else :
    print("test failed")
