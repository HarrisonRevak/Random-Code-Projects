#Harrison Revak
#11/29/2023
#2D Class List

classes = [[1, "Scott", "Comp Sci 1 CC"], [2, "French", "World History"], [3, "Scott", "Personal Finance"], [4, "Mumaw", "Chem H"], [5, "McGarvey", "English H"], [6, "Ricke", "Spanish II H"], [7, "McIntyre", "Algebra II H"]]
print(classes[3])
print(classes[0][1])
print(classes[5][2])
print(classes[6][0])

for x in range(len(classes)):
    print(classes[x])

for x in range(len(classes)):
    print()
    for a in range(3):
        print(classes[x][a], end=" ")
