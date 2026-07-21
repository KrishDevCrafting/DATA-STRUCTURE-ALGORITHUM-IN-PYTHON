# Project 2 : The Perfect Guess
# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the playerʼs guess is higher than the actual number, the program displays “Lower
# number please” .
# Similarly, if the userʼs guess is too low, the program prints “Higher number please” .
# When the user guesses the correct number, the program displays the number of
# guesses the player used to arrive at the number

import random

n = random.randint(1, 100) 
a =  -1
guess = 0
while(a!=n):
    a = int(input("Guess a number between 1 and 100: "))
    guess += 1
    if(a>n):
        print("Lower number please!")
    elif(a<n):
        print("Higher number please!")

print(f"You guessed the number in {guess} attempts and the number was {n}.")