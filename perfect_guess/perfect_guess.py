

import random as r

num = r.randint(1 , 50)

guess =  None

counter : int = 0

while (guess != num):
    try:
        print(f"Attempt number: {counter + 1}")
        guess = int(input("Enter your guess: "))
        counter += 1
        
        if(guess > num):
            print("Your guess is higher, consider lower number")
        
        elif (guess < num):
            print("Your guess is lower, consider a higher number")
        
        else:
            print(f"Congratulations! you guessed the number {num} correctly in {counter} tries")
    
    except ValueError:
        print("Invalid input! Only integers are allowed")

