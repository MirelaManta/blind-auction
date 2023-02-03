from replit import clear

from art import logo

participants = {}
auction_in_progress = True

print(logo)
print("Welcome to Secret Auction Program!")

def find_highest_bidder(bidding_record): 
	max_bid = 0
	winner = ""
	for bidder in bidding_record:
		amount = bidding_record[bidder]
		if amount > max_bid:
			max_bid = amount
			winner = bidder
	print(f"The winner is {winner} with ${max_bid}.")
	
while auction_in_progress:
	bidder_name = input("What is your name?\n")
	bid_amount = int(input("What's your bid?\n$"))
	other_bidders = input("Are there other bidders? Type 'yes' or 'no'. ")
	participants[bidder_name] = bid_amount
	if other_bidders == "no":
		auction_in_progress = False
		find_highest_bidder(participants)
	elif other_bidders == "yes":
		clear()
		
	
	 