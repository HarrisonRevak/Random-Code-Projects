class Candy:
    def __init__(self, a, b, c):
        self.name = a
        self.flavor = b
        self.calories = 100
        self.ok_braces = True
        self.price = c

    def taste(self):
        print(self.name, "candy is", self.flavor)

    def sale_price(self):
        return self.price/2

    def brace(self):
        if self.ok_braces == True:
            print(self.name, "candy is orthodontist approved!")
        else:
            print("You shouldn't eat", self.name, "candy if you have braces.")

    def cost_per_calorie(self):
        if self.calories == 0:
            return 0
        else:
            x = self.price/self.calories
            y = "%.4f"% x
            return y

count = 0


pd = Candy("PayDay", "peanutty", 1.06)
pd.calories = 240
eg = Candy("Extra Gum", "minty", 1.59)
eg.calories=0
fd = Candy("Fun Dip", "fruity", 1.29)
fd.calories = 50
fd.ok_braces = False
sfc = Candy("Starburst Fruit Chews", "fruity", .89)
sfc.calories = 160
sfc.ok_braces = False
st = Candy("Sweet Tarts", "sour", .99)
st.calories = 60
ah = Candy("Air Heads", "fruity", .49)
ah.calories = 120
ah.ok_braces = False
honey = Candy("Bit O' Honey", "honey-flavored", .98)
honey.calories = 150
honey.ok_braces = False


candy_sales=[pd.sale_price(), eg.sale_price(), fd.sale_price(), sfc.sale_price(), st.sale_price(), ah.sale_price(), honey.sale_price()]


pd.taste()

print(pd.name, "candy is on sale today for", pd.sale_price())

pd.brace()

print(pd.name, "candy costs $", pd.cost_per_calorie() ,"per calorie")



print("#1")
print(sfc.name, sfc.calories)

print("#2")
print(eg.name, "candy costs $", eg.cost_per_calorie(),"per calorie")


print("#3")
eg.brace()

print("#4")
print(fd.name, "candy costs $", fd.cost_per_calorie(),"per calorie")

print("#5")
ah.taste()

for i in candy_sales:
    if i < .50:
        count +=1

print("There are", count, "candies in the store that cost less than 50 cents.")
    
    
    






