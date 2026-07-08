# ROCK, PAPAR and SCISSORS GAME:

import random

'''
-1 = ROCK
1 = PAPER
0 = SCISSOR

'''


import random

computer = random.choice([1, -1, 0])

users = input("ENTER YOUR CHOICE: ").lower()

youDIC = {
    "rock": -1,
    "paper": 1,
    "scissor": 0
}

reverseDIC = {
    1: "paper",
    -1: "rock",
    0: "scissor"
}

usersnum = youDIC[users]

print(f"COMPUTER CHOICE: {reverseDIC[computer]}")

if computer == usersnum:
    print("MATCH DRAW!")
else:
    if computer == -1 and usersnum == 1:
        print("YOU WIN!")
    elif computer == 1 and usersnum == -1:
        print("YOU LOSE!")
    elif computer == 1 and usersnum == 0:
        print("YOU WIN!")
    elif computer == 0 and usersnum == 1:
        print("YOU LOSE!")
    elif computer == -1 and usersnum == 0:
        print("YOU LOSE!")
    elif computer == 0 and usersnum == -1:
        print("YOU WIN!")
    else:
        print("Something went wrong!")