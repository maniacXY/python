from replit import clear
from random import randint
from game_data import data
from art import logo, vs

#function random data
def random_data():
    return data[randint(0,len(data)-1)]

#funtion format data to string
def data_format(entry):
    return f"{entry['name']}, a {entry['description']}, from {entry['country']}"

# welcome message
def game ():
    FIRST_ENTRY = random_data()
    SCORE = 0 
    clear()
    print(logo)

    game_running=True
    while game_running:
        entryA = FIRST_ENTRY
        print(f"Compare A: {data_format(entryA)} ")
        print(vs)
        entryB = random_data()
        print(f"Against B: {data_format(entryB)} ")
        correct_answer1 = correct_answer(entryA, entryB)
        user_choice = (input("Who has more followers? Type 'A' or 'B': ")).lower()
        clear()
        print(logo)
        if user_choice == correct_answer1:
            SCORE += 1
            print(f"Your're right! Current score: {SCORE}.")
        else:
            print(f"Sorry, thats wrong. Final score: {SCORE}")
            if (input("Wanna play again? 'y' or 'n'")).lower() == "y":
                game()
            else:
                game_running = False
        
        if correct_answer1 == "b":
            FIRST_ENTRY = entryB

game ()

