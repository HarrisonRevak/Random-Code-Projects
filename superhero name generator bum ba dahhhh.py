aTog = ["A", "B", "C", "D", "E", "F", "G"]
hTon = ["H", "I", "J", "K", "L", "M", "N"]
oTou = ["O", "P", "Q", "R", "S", "T", "U"]
vToz = ["V", "W", "X", "Y", "Z"]

month123 = [1,2,3]
month456 = [4,5,6]
month789 = [7,8,9]
month101112 = [10,11,12]

name = input("Enter your name: ")
month = int(input("What month were you born, input the number: "))

def superheronamefirst(name,month):
    if name[0] in aTog:
        first = "The Fantastic"
    elif name[0] in hTon:
        first = "The Speedy"
    elif name[0] in oTou:
        first = "The Amazing"
    else:
        return "The Incredible"
    if month in month123:
        second = "Shadow"
    elif month in month456:
        second = "Blitz"
    elif month in month789:
        second = "Guy"
    else:
        second = "Bulk"
    return first+ " " +second

print("Your superhero name is ", superheronamefirst(name,month))

