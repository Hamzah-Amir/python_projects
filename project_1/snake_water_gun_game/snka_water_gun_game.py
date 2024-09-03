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

while round <= n:
    
    print(f"Round {round} starts now \n Snake - s \n Water - w \n Gun -g ")

        
    # Conteoling user's input
    
    users_choice = input("Enter your move: ")
    
    # Handling invalid input by user

    if users_choice != "s" and users_choice != "w" and users_choice != "g":
        print("Error You Entered an \"Invalid Move\" Try Again!")
        continue
    
    
    # Giving access to computer to select his move
  
    computer_choice = random.choice(option)
    print(f"Computer chooses {computer_choice}")
    
    # Defining winning and losing conditions

    if computer_choice == "s":
        if users_choice == "w":
            print("Computer win")
            computer_win += 1
        elif users_choice == "g":
            print("User win")
            user_win += 1
        else:
            print("Draw")
    
    if computer_choice == "w":
        if users_choice == "g":
            print("Computer wins")
            computer_win += 1
        elif users_choice == "s":
            print("You win")
            user_win += 1
        else:
            print("Draw")
            
    if computer_choice == "g":
        if users_choice == "s":
            print("Computer win")
            computer_win += 1
        elif users_choice == "w":
            print("User win")
            user_win += 1
        else:
            print("Draw")

    round += 1

# Deciding winner of every round.

if user_win > computer_win:
    print(f"You Won {user_win} Rounds")

if computer_win > user_win:
    print(f"Computer Win {computer_win} Rounds")
else:
    print("Draw")


if user_win > computer_win:
    print(f"Congratulations You Won {round} Rounds!")

 # Viewing Final Winner of Whole Game

if computer_win > user_win:
    print(f"Hardluck! You Lose.")
else:
    print("Match is Draw!")





            

        

    



        

