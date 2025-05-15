import random
print("Welcome to Rock, Paper and Scissor game.\n")
choice=int(input("What would you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor\n"))
game_list=["Rock","Paper","Scissor"]
sys_choice=random.randint(0,2)
if choice==sys_choice:
    print(f"System chose : {game_list[sys_choice]}, Its a draw!!")
elif choice<0 or choice>2:
    print("Invalid choice. Game Over!!")
elif choice==0 and sys_choice==2:
    print(f"System chose : {game_list[sys_choice]}, You win!!")
elif choice==2 and sys_choice==0:
    print(f"System chose : {game_list[sys_choice]}, You loose!!")
elif choice>sys_choice:
    print(f"System chose : {game_list[sys_choice]}, You win!!")

