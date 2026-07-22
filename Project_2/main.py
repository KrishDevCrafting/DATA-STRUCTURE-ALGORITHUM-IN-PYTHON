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

class Person:
    def __init__(self, initial_page: int =1):
     
     self.page = initial_page
    
     self.usersApi = {1:["Ishigami Senku" ,"Suika", "Gen Asagiri"], 2:["Tsukasa ShishiouZoro", "Hyoga"], 3:["Dr Xeno.."]}
    
    def fetch_user_batch(self) -> list[str]:
       '''Fetches a batch of users from the simulated API.'''
       batch = self.usersApi.get(self.page, [])
       self.page += 1  # Move to the next page for the next call
       return batch 
    
    # Initialize the Object.....
fetcher = Person()

    # Using the walrus operator to fetch and process users in a loop

while users := fetcher.fetch_user_batch():
        print(f"Processing page {fetcher.page - 1}: {users}") 

# Types Definition in python:
age: int = 25 

def greeting(name: str) ->str:
    return f"Hiiiiiiiiiiiiiiiiii,{name}"
print(greeting("Radha...."))