print("Welcome to python Pizza deliveries!")
size=input("What size of pizza do you want? S,M or L?\n").lower()
pepperony=input("Do you want pepperoni on your pizza? Y or N : \n").lower()
extra_cheese=input("Do you want extra cheese? Y or N : \n").lower()

if size=="s":
    final_price=15
    if pepperony=="y":
        final_price+=2
elif size=="m":
    final_price=20
    if pepperony=="y":
        final_price+=3
else:
    final_price=25
    if pepperony=="y":
        final_price+=2
if extra_cheese=="y":
    final_price+=2

print(f"Final price of Pizza : {final_price}")