def main():
    print("Currently you are in a room and there are two doors in front of you")
    print("1. Red")
    print("2. Blue")
    print("Which door do you want to pick ?")
    door_pick = input("Enter Which Door: ")
    if door_pick == "red" or door_pick == "1":
        red_door()
    elif door_pick == "blue" or door_pick == "2":
        blue_door()
    else:
        print("you idiot its either red or blue")
        return pg()

def pg():
    door_pick = input("Enter Which Door: ")
    if door_pick == "red" or door_pick == "1":
        red_door()
    elif door_pick == "blue" or door_pick == "2":
        blue_door()
    else:
        print("you idiot its either red or blue")
        return pg()

def red_door():
    print("There is a Dragon in front of you")
    print("What do you want to do")
    print("Leave or Stay")
    los_pick = input()
    if los_pick == "leave":
        pg()
    elif los_pick == "stay":
        print("You got eaten by the Dragon you are just very Dumb")
        return
    else:
        print("you idiot choose if you want to leave or stay")
        return rd_pg()

def rd_pg():
    los_pick = input()
    if los_pick == "leave":
        pg()
    elif los_pick == "stay":
        print("You got eaten by the Dragon you are just very Dumb")
        return
    else:
        print("you idiot choose if you want to leave or stay")
        return rd_pg()

def blue_door():
    print("There is a Treasure in front of you")
    print("Do you want to open it?")
    treasure_choice = input()
    if treasure_choice == "yes":
        print("You got the Treasure that was lost 5000 years ago, congo")
        return
    elif treasure_choice == "no":
        print("You lost the chance to get the Treasure with valuable items you dumb fool")
        return
    else:
        print("you idiot its a simple yes or no")
        return bd_pg()

def bd_pg():
    treasure_choice = input()
    if treasure_choice == "yes":
        print("You got the Treasure that was lost 5000 years ago, congo")
        return
    elif treasure_choice == "no":
        print("You lost the chance to get the Treasure with valuable items you dumb fool")
        return
    else:
        print("you idiot its a simple yes or no")
        return bd_pg()

main()