def calculate_love_score(name1,name2):
    combined_name=name1+name2
    name_in_lower=combined_name.lower()

    t =name_in_lower.count("t")
    r = name_in_lower.count("r")
    u = name_in_lower.count("u")
    e = name_in_lower.count("e")
    first_digit=t+r+u+e

    l = name_in_lower.count("l")
    o = name_in_lower.count("o")
    v = name_in_lower.count("v")
    e = name_in_lower.count("e")
    second_digit=l+o+v+e

    score=int(str(first_digit)+str(second_digit))
    return score

print("Welcome to love calculator!")
first_name=input("Enter your name : ")
second_name=input("Enter your lover's name : ")

print(f"Your love score is : {calculate_love_score(first_name,second_name)}")
