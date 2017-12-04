
class user():
    calories = float(input("Whats your calories requirements?"))
    protein = float(input("Whats your protein requirements?"))
    carbs = float(input("Whats your carbs requirements?"))
    fat = float(input("Whats your fat requirements?"))


class chicken():
    grams = 100
    calories = 150
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

saladR = salad.calories / salad.protein
chickR = chicken.calories / chicken.protein
Co = user.protein - 1
Ct = 1


while True :
    x = Co * saladR
    y = Ct * chickR
    total = x + y
    if total == user.calories :
        Sfo = Co / salad.protein
        Sft = Ct / chicken.protein
        A = Sfo * salad.grams
        B = Sft * chicken.grams
        print("you need ", "%.2f" % A, " grams of salad to meet your needs ")
        print("you need ", "%.2f" % B, " grams of Chicken to meet your needs ")
        break
    else :
        Co -= 1
        Ct += 1

print("check")