from replit import clear
from art import logo
#TODO make it a bit userfriendlier ...

#TODO make it cleaner no need of the double alphabet cus of the % check at the bottom 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

programm_running = True
while programm_running:
  print (logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #TODO can be cleaner !!! make it independent from the number
  shift = shift % 26
    
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  again = input("You wanna restart type:'yes' or 'no' for quit:\n")
  if again == "yes":
    programm_running = True
    clear()
  else:
    print ("You quit")
    programm_running = False

