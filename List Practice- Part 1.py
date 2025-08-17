golfscores = [78,81,75,86,74]
print(golfscores)
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
print(colors)
recipes = ["vegetable lasagna", "red curry", "jambalaya", "chicken enchiladas", "falafel"]
print(recipes)
teachers = ["Kristin Scott", "George French", "Dennis Scott", "Clark Mumaw", "Nathan McGarvey", "Jensen Ricke", "Chris McIntyre"]
print(teachers)
desserts = ["frozen yogurt", "bread pudding", "hummingbird cake", "baklava", "apple pie", "churros"]
print(desserts)
testScores = [99,86,65,100,91,76]
print(testScores)

print("#1")
print(golfscores[0])
colors[5]="Indigo"
colors.append("Violet")
print("#3")
for items in colors:
    print(items)
recipes[2]="macaroni"
desserts[0]="ice cream"
print("#6")
for items in teachers:
    print(items)
print("#7")
for x in range(len(desserts)):
    print(desserts[x])
print("#8")
print(recipes, end="")

print()
print("#10")

sum=0
for i in range(len(testScores)):
    sum+=testScores[i]


average=sum/len(testScores)
print(average)






print()
print()
print()


videogame = ["Terraria ","SlimeRancher ","ProjectZomboid ","Foxhole ","Barotrauma "]
print("#1")
print(videogame)
print("#2")
print(videogame[4])
print("#3")
videogame.append("FiveNightAtFreddy")
print("#4")
for item in videogame:
    print(item)
print("#5")
for x in range(len(videogame)):
    print(videogame[x], end="")





















