print("Welcome to tip calculator!")
final_bill=float(input("What was the total bill? $"))
tip=int(input("how much tip would you like to give? 10,12 or 15?"))
no_of_people=int(input("How many people are to split the bill?"))
bill_per_person=(final_bill+tip)/no_of_people
print(f"Final share per person is :  ${bill_per_person}")