food = [["Chic Fil A", "Zaxby\'s", "Popeye\'s", "Famous Recipe"], ["McDonald\'s", "DQ", "Burger King", "Five Guys"], ["Quizno\'s", "Subway", "Jersey Mike\'s", "Potbelly"]]
print("#1")
print(food[1])
print("#2")

for x in range(len(food)):
    print()
    for y in range(len(food[x])):
        print(food[x][y], end=" ")
food[0][3]= "KFC"
food[2][3]= "Penn Station"
print()
print("#3")
for x in range(len(food)):
    print(food[x][3])
