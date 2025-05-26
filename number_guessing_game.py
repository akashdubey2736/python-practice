import random

print("Welcome to number guessing game !")
print("I am thinking of a number between 1 and 100.")

GENERATED_NUMBER=random.randint(1,101)
difficulty_level=input("Choose a difficulty level. Type 'easy' or 'hard : \n").lower()
if difficulty_level=="easy":
    attempts=10
elif difficulty_level=="hard":
    attempts=5
else:
    print("Invalid difficulty level. Please choose 'easy' or 'hard " )

while attempts>0:
    print(f"You have {attempts} remaining attempts to guess the number.")
    guess=int(input("Make a guess : "))
    if guess==GENERATED_NUMBER:
        print(f"You got it! answer was : {GENERATED_NUMBER}.")
    elif guess<GENERATED_NUMBER:
        print("Too low.\n")
    elif guess>GENERATED_NUMBER:
        print("Too high.\n")
    attempts-=1
    if attempts==0:
        print(f"You have run out of guesses. You loose! Number was : {GENERATED_NUMBER}")
    else:
        print("Guess again!")

