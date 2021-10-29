from replit import clear
from art import logo


# works but ugly !!!
# bids_dic = {}
# print(logo)
# print("Welcome to the secret auction program")
# running = True
# while running:
#   name = input("What is your name?: ")
#   bid = int(input("What is your bid?: "))
#   bids_dic[name] = bid
#   go_on = input("Are there any other bidders? Type 'yes' or 'no'.\n")
#   if go_on == "yes":
#     clear()
#   elif go_on == "no":
#     highets_bid = 0
#     highest_name = ""
#     for name in bids_dic:
#       if bids_dic[name] > highets_bid:
#         highets_bid = bids_dic[name]
#         highest_name = name
#     clear()
#     print(f"The highest bid comes from {highest_name} with ${highets_bid}")
#     running=False
#   else:
#     print("Parameter not definde!")
#     running = False

# just passing the if into a function
print(logo)
bids = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
while not bidding_finished:
  name = input("What is your name? ")
  price = int(input("What is your bid? $"))
  bids [name] = price
  should_continue = input("Any other bidders? Type 'yes' or 'no' ")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()






