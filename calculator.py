def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={"+":add,"-":subtract,"*":multiply,"/":divide}

should_continue=True

number_1=float(input("Enter first number : "))
while should_continue:
    for operation in operations:
        print(operation)
    choice=input("Choose one of the operation from above : ")
    number_2=float(input("Enter second number : "))
    answer=operations[choice](number_1,number_2)
    print(f"{number_1} {choice} {number_2} = {answer}")
    next=input("Type 'y' to continue with answer or 'n' to start again")
    if next=="y":
        number_1=answer
    else:
        should_continue=False





