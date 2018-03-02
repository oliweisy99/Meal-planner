'''
calculates how much grams of chicken you need to match your requirements of calories for it to 3 decimal places

if user.calories == chicken.calories :
    print("test success")
else :
   holder = user.calories / chicken.calories
    amount = holder * chicken.grams
   print("%.3f" % amount, " grams of chicken for ", user.calories, " required calories")

holderone = user.calories / salad.calories
holdertwo = user.calories / chicken.calories
holderone = holderone / 2
holdertwo = holdertwo / 2
amountone = holderone * salad.grams
amounttwo = holdertwo * chicken.grams
print("%.3f" % amountone, " - this is the amount of grams for salad")
print("%.3f" % amounttwo, " - this is the amount of grams for chicken")
 this works out how much calories is needed for two foods.


def repeat(inputo,inputt) :
    A = (inputo / salad.protein) * salad.grams
    B = (inputt / chicken.protein) * chicken.grams
    print("you need ", "%.2f" % A, " grams of salad to meet your needs ")
    print("you need ", "%.2f" % B, " grams of Chicken to meet your needs ")

while True :
    Co -= 1
    Ct += 1
    H = Co - 1 # this is the one after going through the list of possiblities
    T = Ct + 1
    x = Co * saladR # counts multiplied by ratios to find calorie amount
    y = Ct * chickR
    total = x + y
    sum = ((H * saladR) + (T * chickR)) - user.calories
    Tmu = total - user.calories
    if total == user.calories : # if total is equal to the required calorie amount
        repeat(Co, Ct)
        break
    else :
        if Tmu > 0 :
            if sum < Tmu :
                continue
            else :
                repeat(H, T)
                break
        else :
            temp = user.calories - total
            if temp > sum :
                continue
            else :
                repeat(H, T)
                break

# next stage is adding in more foods, do 5 foods to create one meal, then do that for carbs and fat
# after that, start creating
'''
