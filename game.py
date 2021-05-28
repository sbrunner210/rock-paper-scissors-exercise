# game.py

# Importing random for the computer's choice.
import random
# Importing os and dotenv to properly utilze the .env file.
import os
import dotenv

# Identifying that there is a .env file.
dotenv.load_dotenv()

# Pulling the information from the .env file.
player_name = os.getenv("user")

print (f"Welcome {player_name} to Rock, Paper, Scissors!")

print("-----------------------------")
print("Rock, Paper, Scissors, Shoot!")
print("-----------------------------")

# Prompting the user to make an input.
user_choice = input("Please choose one of 'rock' , 'paper', 'scissors': ")

print("-----------------------------")
print("USER CHOICE: ",user_choice)
print("-----------------------------")

# validate the input such that only if it is one of the accepted inputs...
#... we will continue with the rest of the program. Otherwise, we'll stop ...
#... the program before it tries to do anything else and ask the program ...
#... to run again

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print ("Good choice!")
else:
    print("Oops! Invalid input. Please try again.")
    exit()

# Lists the options for the computer to choose from. Uses random choice to select computer's choice. This needs to be imported.
valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options)

print("-----------------------------")
print("COMPUTER CHOICE: ", computer_choice)
print("-----------------------------")

# This is the logic for the game.
if user_choice == computer_choice:
    print ("IT'S A TIE!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print (f"{user_choice} > {computer_choice} YOU WIN!")
    if computer_choice == "paper":
        print (f"{user_choice} < {computer_choice} YOU LOSE! :(")
elif user_choice == "paper":
    if computer_choice == "rock":
        print (f"{user_choice} > {computer_choice} YOU WIN!")
    if computer_choice == "scissors":
        print (f"{user_choice} < {computer_choice} YOU LOSE! :(")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print (f"{user_choice} > {computer_choice} YOU WIN!")
    if computer_choice == "rock":
        print (f"{user_choice} < {computer_choice} YOU LOSE! :(")
else:
        print ("ERROR")  
        exit()    

# End of script.
print("This is the end of our game. Please play again!")