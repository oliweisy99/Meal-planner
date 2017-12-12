
class user():
    calories = float(input("Whats your calories requirements?"))
    protein = float(input("Whats your protein requirements?"))

class chicken():
    grams = 100
    calories = 150
    protein = 10

class salad():
    grams = 100
    calories = 75
    protein = 15

user()

saladR = salad.calories / salad.protein
chickR = chicken.calories / chicken.protein
Co = user.protein
Ct = 0
"""
creates ratios and counts
"""

uc = user.calories
total = Co * saladR
if total < uc :
    need = uc - total
else : 
    need = total - uc
stepV = chickR - saladR
if stepV < 0 :
    stepV = stepV * -1
minA = need // stepV
A = ((Co - minA) / salad.protein) * 100
B = ((Ct + minA) /  chicken.protein) * 100
print("you need ", "%.2f" % A, " grams of salad to meet your needs ")
print("you need ", "%.2f" % B, " grams of Chicken to meet your needs ")

'''
works out need for two foods for calorie and protein 
'''
