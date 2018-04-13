class food:
    def __init__(self):
        self.name = ""
        self.grams = 0
        self.cals = 0
        self.pros = 0
        self.carbs = 0
        self.fats = 0
      # self.attributes = []

nom = "steak"

list = [0] * 50
list[0] = food()
list[0].name = nom
list[0].grams = 100
print(list[0].name)
print(list[0].grams)
