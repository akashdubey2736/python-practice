def name_formatter(fname,lname):
    return fname.capitalize()+" "+lname.capitalize()

fname=input("Enter your first name :")
lname=input("Enter your last name: ")
print("Your formatted name is : "+name_formatter(fname,lname))