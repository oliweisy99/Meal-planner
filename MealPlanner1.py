
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
# creating ratio for the salad for calories to  protein
chickR = chicken.calories / chicken.protein
# creating ratio for the chicken for calories to protein
Co = user.protein - 1
# setting the counts to go through all the possibilities
Ct = 1


while True :
    x = Co * saladR # counts multiplied by ratios to find calorie amount
    y = Ct * chickR
    total = x + y
    if total == user.calories : # if total is equal to the required calorie amount
        Sfo = Co / salad.protein # working out the scale factors to multiply all food details by
        Sft = Ct / chicken.protein
        A = Sfo * salad.grams
        B = Sft * chicken.grams
        print("you need ", "%.2f" % A, " grams of salad to meet your needs ")
        print("you need ", "%.2f" % B, " grams of Chicken to meet your needs ")
        break
    else :
        # incrementing and decrementing the counts to find the amount needed
        Co -= 1
        Ct += 1
    # elif total < user.calories
        # need to work out how to find the best approximation
        # compare the totals with each other, so modify the counts to the previous one and the one after to compare it
        # maybe also find a way of jumping the count to speed up the efficiency so it doesnt have to go through every
        # possibility, this will make it easier when there are more foods to deal with...
        # maybe focus on that when you introduce more foods and more requirements.
        # introduce more foods first, then find a way of introducing loads of foods, still using protein and Kal
        # then introduce ways of working out with carbs and fat also
        # then when you can do that, move on to the next stage of creating meals - lunch, breakfast, etc

print("check")