room_list=[]
room = ["You are in a dark living room, the only light coming from a small TV.\nInfront of you a coffee table and behind a sofa.\nYou can move to your right.", None, 1, None, None]
room_list.append(room)#0
room = ["You are in a long hallway running through the apartment, a few picture frames line the walls.\nYou can move in every direction.", 5, 2, 3, 0]
room_list.append(room)#1
room = ["You are in a small, compact kitchen.\nA hum comes from the fridge crammed in the corner, kitchen utensils litter the counter.\nYou can only go back the way you came.", None, None, None, 1]
room_list.append(room)#2
room = ["You are in a near pitch black room, a computer on its screensaver in the corner the only light.\nThe bed is stripped of the sheets and pillows, in the corner a closet.\nYou can go back to the hall or to the closet on your left.", 1, None, None, 4]
room_list.append(room)#3
room = ["You are crammed in a small closet, as far as you can see only old clothes sit inside.\nYou can only leave.", None, 3, None, None]
room_list.append(room)#4
room = ["You are in a foyer, a table by the front door.\nA coat rack sits opposite of it, nothing is on it.\nYou can go in every direction.", 8, 6, 1, 7]
room_list.append(room)#5
room = ["You are in a bathroom, a bathtub behind you, a toilet to your right and a sink infront of you with a mirror above it.\nYou can only go back the way you came.", None, None, None, 5]
room_list.append(room)#6
room = ["You are on the balcony, overlooking the city.\nAs far as you can see, all the lights to the city are off.\nNothing is on the balcony.\nYou can only go back the way you came,", None, 5, None, None]
room_list.append(room)#7
room = ["You push the door open, into the dark night.\nYou've finally gotten out of the apartment, but something feels off.\nIt's quiet.", None, None, 5, None]
room_list.append(room)#8
current_room=0
#next_room=[current_room][0]
done=False
#loop intro
while not done:
    print()
    print(room_list[current_room][0])
    desire = input("What would you like to do? ")
    #directions
    if desire.lower() == "n" or desire.lower() =="north": #north
        next_room=room_list[current_room][1] # you only need ONE equal sign here
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room=next_room   # you only need ONE equal sign here
    elif desire.lower() == "e" or desire.lower() =="east": #east
        next_room=room_list[current_room][2]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room=next_room
    elif desire.lower() == "s" or desire.lower() =="south": #south
        next_room=room_list[current_room][3]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room=next_room
    elif desire.lower() == "w" or desire.lower() =="west": #west
        next_room=room_list[current_room][4]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room=next_room
            
    if current_room == 8: #exit
        print()
        print(room_list[current_room][0])
        done = True

    
