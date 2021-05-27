# game.py

import random
import os
# from dotenv import load_dotenv

#load_dotenv()

# player_name = os.getenv(user)

# print (player_name)
print("-----------------------------")
print("Rock, Paper, Scissors, Shoot!")
print("-----------------------------")

user_choice = input("Please choose one of 'rock' , 'paper', 'scissors': ")

print("-----------------------------")
print("USER CHOICE: ",user_choice)
print("-----------------------------")


# validate the input such that only if it is one of the accepted inputs...
#... we will continue with the rest of the program. Otherwise, we'll stop ...
#... the program before it tries to do anything else and ask the program ...
#... to run again

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print ("GOOD CHOICE!")
else:
    print("OOPS, INVALID INPUT. PLEASE TRY AGAIN.")
    exit()

valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options)

print("-----------------------------")
print("COMPUTER CHOICE: ", computer_choice)
print("-----------------------------")

if user_choice == computer_choice:
    print ("IT'S A TIE!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print (user_choice, ">", computer_choice, "YOU WIN!")
    if computer_choice == "paper":
        print (user_choice, "<", computer_choice, "YOU LOSE! :(")
elif user_choice == "paper":
    if computer_choice == "rock":
        print (user_choice, ">", computer_choice, "YOU WIN!")
    if computer_choice == "scissors":
        print (user_choice, "<", computer_choice, "YOU LOSE! :(")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print (user_choice, ">", computer_choice, "YOU WIN!")
    if computer_choice == "rock":
        print (user_choice, "<", computer_choice, "YOU LOSE! :(")
else:
        print ("ERROR, YOU SCREWED UP IDIOT!")      




print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN!")