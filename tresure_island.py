print("Welocme to Tresure Island.\n")
print("Your mission is to find the Treasure.\n")
choice=input("You are at crossroads. Do you want ot go to left or right? ")
if choice=="left":
    choice=input("Do you want to swim or wait? ")
    if choice=="swim":
        print("You are attacked by Lion. Game Over!!")
    elif choice=="wait":
        choice=input("Which door do you want to open? red, blue or yellow ?")
        if choice=="red":
            print("you are burnt by file. Game over!!")
        elif choice=="blue":
            print("You are beaten by Beasts. Game Over!!")
        elif choice=="yellow":
            print("You have found the Treasure. You Win!!")
        else :
            print("Invalid choice. Game Over!!")
    else:
        print("Invalid choice. Game Over!!")
elif choice=="right":
    print("You fell in hole. Game Over!!")
else:
    print("Invalid choice. Game Over!!")