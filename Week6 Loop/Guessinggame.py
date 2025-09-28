# Number guessing game - program picks a number; user guesses until, using a loop
# the user guesses correctly

import random
number = random.randint(1, 100)  # pick a number between 1 and 100
guess = 0  # initialize the user's guess to a value that is not the number
tries = 0  # initialize the number of tries to 0
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
while guess != number:  # loop until the user guesses the number
    guess = int(input("Enter your guess: "))  # get the user's guess
    tries += 1  # increment the number of tries
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {tries} tries.")
        break  # exit the loop if the user guessed correctly    
print("Thanks for playing!")
# end of program

