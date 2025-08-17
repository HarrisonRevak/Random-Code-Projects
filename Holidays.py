holiday = ["MLK Jr Day", "Presidents Day", "Mothers Day", "Memorial Day", "Fathers Day", "Labor Day", "Thanksgiving"]
date = ["third Monday in January","third Monday in Feburuary", "second Sunday in May", "last Monday in May", "third Sunday in June", "first Monday in September", "fourth Thursday in November"]
answer=""
pos=0

answer = input("Enter a holiday: ").lower()
for x in range(len(holiday)):
    if holiday[x].lower()==answer:
        pos=x
print(date[pos])

    
