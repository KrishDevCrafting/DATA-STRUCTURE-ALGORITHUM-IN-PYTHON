# Project 2 : The Perfect Guess
# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the playerʼs guess is higher than the actual number, the program displays “Lower
# number please” .
# Similarly, if the userʼs guess is too low, the program prints “Higher number please” .
# When the user guesses the correct number, the program displays the number of
# guesses the player used to arrive at the number

# import random

# n = random.randint(1, 100) 
# a =  -1
# guess = 0
# while(a!=n):
#     a = int(input("Guess a number between 1 and 100: "))
#     guess += 1
#     if(a>n):
#         print("Lower number please!")
#     elif(a<n):
#         print("Higher number please!")

# print(f"You guessed the number in {guess} attempts and the number was {n}.")
# ////////////////////////////////////////
# Chapter 12 Advanced Python Programming

# walrus operator == Assigment expression hai

# Assigns a value to a variable and returns that value in a single step (inside an expression).


# (variable := expression)

def fetch_user_batch(page: int) -> list[str]:
    # Simulates an API call that returns empty list on page 4
    api_db = {1: ["Alice", "Bob"], 2: ["Charlie", "David"], 3: ["Eve"]}
    return api_db.get(page, [])

page = 1
users = fetch_user_batch(page)  # 1st call

# Assigns 'users' and checks 'bool(users)' in a single evaluation
while users := fetch_user_batch(page):
    print(f"Processing page {page}: {users}")
    page += 1

