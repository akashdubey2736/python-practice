print("Welcome to secret auction program")
bids={}
bidding_finished=False
while not bidding_finished:
    name=input("Enter your name : ")
    bid_amount=int(input("Enter your bid amount : "))
    bids[name]=bid_amount
    choice=input("Do you want to continue bidding? Type 'yes' to continue or 'no' ").lower()
    if choice=="no":
        bidding_finished=True

highest_bid=0
winner=""
for name in bids:
    if highest_bid<bids[name]:
        highest_bid=bids[name]
        winner=name

print(f"Winner is {winner} with bid amount of {bids[winner]}")


