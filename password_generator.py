import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H',
         'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']

print("Welcome to password generator\n")
number_of_letters=int(input("Enter the number of letters required : "))
number_of_numbers=int(input("Enter the number of numbers required : "))
number_of_symbols=int(input("Enter the number of symbols required : "))

password_list=[]
for char in range(1,number_of_letters+1):
    password_list.append(random.choice(letters))
for char in range(1,number_of_letters+1):
    password_list.append(random.choice(numbers))
for char in range(1,number_of_symbols+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password=""
for char in password_list:
    password+=char

print(f"Generated password is : {password}")