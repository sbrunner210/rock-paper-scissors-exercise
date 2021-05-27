# game.py

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock' , 'paper', 'scissors': ")

print("USER CHOICE: ",user_choice)

# validate the input such that only if it is one of the accepted inputs...
#... we will continue with the rest of the program. Otherwise, we'll stop ...
#... the program before it tries to do anything else and ask the program ...
#... to run again

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print ("VALID. KEEP GOING")
else:
    print("OOPS, INVALID INPUT. PLEASE TRY AGAIN.")
    exit()

print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN!")