# Project 01 Write a program for Snake Water Gun Game

import random  #Importing random module

head = "snake water gun game"

print(head.title())

n = int(input("Enter the number of rounds: "))

options = ["s", "w", "g"]

round = 1

# Users no of rounds won 

users_win = 0

#Computers no of rounds won

computers_win = 0

# USing while loop to start the game

while (round <= n):

    # Dsplaying current round
    
    print(f"Round no {round} starts \n snake - s \n water - w \n gun - g")

    try:
          
          users_choice = input("Enter Your Move: ")

    except EOFError as error:
        print(error)

        # COntrolling invalid inputs
        if (users_choice != "s" and users_choice != "w" and users_choice != "g"):
             print("Error \"Invalid Input\" Try Again!")
             continue
    
    # Giving access to computer to select random options
    
    computers_choice = random.choice(options)

    # Giving win and lost conditions

    if computers_choice == "s":
         if users_choice == "w":
              computers_win += 1
         
         elif users_choice == "g":
              users_win =+1

    if computers_choice == "w":
         if users_choice == "g":
              computers_win +=1

         elif users_choice == "s":
              users_win +=1
    
    if computers_choice == "g":
         if users_choice == "s":
              computers_win +=1

         elif users_choice == "w":
              users_win +=1
              



         
                       
         
        


  

    # ENabling exceptions for invalid input.


