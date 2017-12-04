
# calculates how much grams of chicken you need to match your requirements of calories for it to 3 decimal places

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
# this works out how much calories is needed for two foods.