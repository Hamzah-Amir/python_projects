# Project 1: Create Snake, Water And gun game with python

import random

head = "Snake Water Gun Game"
print(head.title())

n = int(input("Enter the no of Rounds: "))

option = ["s", "w", "g"]

round = 1

# Storing computer' & User's Win

computer_win = 0

user_win = 0

# Using while loops to start the game again & again

while (round <= n):
    print(f"Round {round} starts now \n Snake - s \n Water - w \n Gun -g ")

    # Conteoling user's input

    try:

        users_choice = input("Enter your move: ")
    except EOFError as e:
        print(e)
    
    # Handling invalid input by user

    if users_choice != "s" and users_choice != "w" and users_choice != "g":
        print("Error You Entered an \"Invalid Move\" Try Again!")

    # Giving access to computer to select his move

    computer_choice = random.choice(option)

    # Defining winning and losing conditions

    if computer_choice == "s":
        if users_choice == "w":
            computer_win += 1
        elif users_choice == "g":
            user_win += 1

    
    if computer_choice == "w":
        if users_choice == "g":
            computer_win += 1
        elif users_choice == "s":
            user_win += 1


            
    if computer_choice == "g":
        if users_choice == "s":
            computer_win += 1
        elif users_choice == "w":
            user_win += 1

# Deciding winner of every rounf.

if user_win > computer_win:
    print(f"Congratulations You Won {round} Rounds!")

if computer_win > user_win:
    print(f"Hardluck! You Lose.")
else:
    print("Match is Draw!")





            

        

    



        

