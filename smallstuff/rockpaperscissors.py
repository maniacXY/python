import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
computer = random.randint(0,2)
print("Hello and welcome to Rock-Paper-Scissors\nWhat is your choice?\n")
player = (int(input("1.rock\n2.paper\n3.scissors\n")) - 1)

if player > 2:
  print("Are you an idiot?")
else:
  print(f"Players Choice\n {options[player]}\n")
  print(f"Computers Choice\n {options[computer]}\n")

  if player == computer:
    print ("Unentschieden")
  elif player == 0 and computer == 1:
    print ("Computer Wins")
  elif player == 0 and computer == 2:
    print ("Player wins")
  elif player == 1 and computer == 0:
    print ("Player wins")
  elif player == 1 and computer == 2:
    print ("Computer wins")
  elif player == 2 and computer == 0:
    print ("Computer wins")
  elif player == 2 and computer == 1:
    print("Player wins")
