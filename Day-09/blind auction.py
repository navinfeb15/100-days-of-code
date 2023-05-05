from art import logo

print(logo)

bid = {}
bidding_finished = False

while not bidding_finished:
  # Function to find the highest bidder
  def find_highest_bidder(bid):
    highest_price = 0
    highest_bidder = ""
    for bidder in bid.keys():
      if bid[bidder] > highest_price:
        highest_price = bid[bidder]
        highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_price}")

  # Ask the user for their name and bid
  name = input("What is your name?: ")
  price = int(input("What is your bid?: "))
  bid[name] = price
  # Ask if there are any other bidders
  should_continue = input("Are there any other bidders? Type 'yes' or 'no' \n")
  
  # For clearing screen
  print('\033[2J\033[H')

  # If there are no other bidders, find the highest bidder and end the loop
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bid)

