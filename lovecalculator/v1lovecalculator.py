from art import bye, logo, output
from replit import clear
list = ["true", "love"]
# Input the names

game = True
while game:
  clear()
  print(logo)  
  name1 = input("What is your name? \n")
  name2 = input("What is their name? \n")
  combinedname = (name1 + name2).lower()

  true = 0
  love = 0

  for letter in combinedname:
    if letter in list[0]:
      true += 1
    if letter in list[1]:
      love += 1
  result = int(str(true) + str(love))
  clear()
  print(output)
  if result < 10 or result > 90:
    print(f"Your score is {result}, better marry your cat!")
  elif result >= 40 and result <= 50:
    print(f"Your score is {result} hrrrrrrrr ...")
  else: 
    print (f"Your score is {result}.")
  if not input("Wanna play again? 'y' :") == "y":
    game = False
    clear()
    print(bye)



