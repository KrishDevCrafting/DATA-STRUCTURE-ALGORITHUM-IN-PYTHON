# import pyjokes

# variable = pyjokes.get_joke()

# print(variable)


a = 5
b = 10

print(a % b)



a1 = 34
b2 = 80

print(a1>b2)

Name = "KRISH"

shortName = Name[0:3]

print(shortName)


value = "Hey \" Krish\" what's going \n on did you finish your homework or not?"

print(value)

# name = input("Enter your Name plz..")

# print(f"Hii My Handsome {name}")

word = "Krish"

print(word[1:6:2])


arry = ["krish",1,0.25,True,'Apple'];

arry.insert(3, "Napolean-Hill")
print(arry)


ab = (1,)

print(type(ab))



fruits = []


# f1 = input("Enter the fruits..")
# fruits.append(f1)



# for i in range(5):
#     print(i)


# for y in range(1,11):
#     if y % 2 == 1:
#         print(y)
# for x in range(0,7):
#     f1 = input("Enter the Fruits..")
#     fruits.append(f1)
#     print(fruits)



# numberOfstudents = []

# for marks in range(0,6):
#  ab1 = input("Enter the Marks of the Studens!")
#  numberOfstudents.append(ab1)

#  numberOfstudents.sort()

#  print(numberOfstudents)

marks = {
    "KRISH" : 99,
    "Gender" : "Male",
    "Expertise" : "Racing Racing aur Cars++"

}


print(marks.items())
print(marks.values())

# s = set()
# print(s)

# s = set()
# v = input("ENTER THE NUMBER!")
# s.add(int(v))
# v = input("ENTER THE NUMBER!")
# s.add(int(v))
# v = input("ENTER THE NUMBER!")
# s.add(int(v))
# v = input("ENTER THE NUMBER!")
# s.add(int(v))
# v = input("ENTER THE NUMBER!")
# s.add(int(v))
# v = input("ENTER THE NUMBER!")
# s.add(int(v))
# v = input("ENTER THE NUMBER!")
# s.add(int(v))
# print(s)


# Dictonary!
# fn = {}
# words = input("Enter friends name:")
# meaning = input("Enter Language name:")

# fn.update({words:meaning})

# print(fn)
 
 






# Name Listed Program...
# name = ["Krish","Rachit,Aarushi","Deepak"]

# EnterInput = input("Enter the name:")

# if(EnterInput in name):
#     print("Your Name is listed!")
# else: 
#     print("Fuck-Off..")


# LOOP in py

for counting in range(1,11):
    print("numbers",counting)




kk = ["Harry", "Coke", "Diet_coke", "pepsi", "KFC", "Sting"]

i = 0

while i < len(kk):
    print(kk[i])
    i += 1

print(len(kk))


list = [1,2,3,4,5,7,8,9,10]

for item in list:
    print(item)
else:
    print("done")
    # Write a program to find the greatest of four numbers entered by the user.

    # a = int(input("Enter the Number!"))
    # b = int(input("Enter the Number!"))
    # c = int(input("Enter the Number!"))
    # d = int(input("Enter the Number!"))




    # Output = max(a,b,c,d)

    # print(Output,"greatest_Number")


    # 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.



    # marks1 = int(input("Enter the Marks of the student!"))
    # marks2 = int(input("Enter the Marks of the student!"))
    # marks3 = int(input("Enter the Marks of the student!"))

    # total_percentage = (marks1 + marks2 + marks3) / 3

    # if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    #     print("You passed!")
    # else:
    #     print("You failed!")


#  A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# comment = input("Enter Your Comment: ").lower()

# if ("make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment or "click this" in comment):
#     print("Spam Comments!")
# else:
#     print("Not a Spam comment. Good to go!")

# Write a program to find whether a given username contains less than 10 characters or not.

# username = input("Enter the Username ")

# if len(username) > 10:
#     print("Characters is not less than 10")
# else: 
#     print("Not...")


# '''Write a program to calculate the grade of a student from his marks from the following
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F'''

# GradeCal = int(input("Enter the Grade Score..."))

# if GradeCal >= 90 and GradeCal <=100:
#     print("Ex")
# elif GradeCal >=80:
#     print("A")

# elif GradeCal >=70:
#     print("B")

# elif GradeCal >=60:
#     print("C")
# elif GradeCal >=50:
#     print("D")
# else:
#     print("Next try better...")

# 7. Write a program to find out whether a given post is talking about “Harry” or not.


# post = input("Enter the post comment...").lower()

# if "harry" in post:
#     print("Talking about Harry")
# else:
#     print("Not talking about Harry")


# table = int(input("Enter a Number!"))

# for i in range(1,11):
#     print(f"{table} * {i} = {table*i}")


# list

# names = ["Harry","Soham","Sachin","Rahul"]

# for name in names:
#     if name.startswith("S"):
#         print(f"Hello {name}")

# Prime or not

# primeNumer = int(input("Enter the number plz.."))

# for i in range(2,primeNumer):
#     if(primeNumer%i) == 0:
#         print("It's a prime number..")
#         break
#     else:
#         print("Not a Prime number..")


# primeNumber = int(input("Enter the number plz.. "))

# if primeNumber < 2:
#     print("Not a Prime number..")
# else:
#     for i in range(2, primeNumber):
#         if primeNumber % i == 0:
#             print("Not a Prime number..")  # Divisible hai → NOT prime
#             break
#     else:
#         # Yeh for-else hai — jab loop bina break ke finish ho, tab chale
#         print("It's a Prime number..")  # Kisi se divide nahi hua → Prime!

# Natural number Sum:
# n = int(input("Enter the natural number:"))


# i = 1
# sum = 0
# while(i<=n):
#     sum += i
#     i +=1
    
# print(sum)

# find Factorial Number 1*2*3*4*5

# f = int(input("Enter the Real number!"))

# product = 1
# for i in range(1,f+1):
#     product = product * i
# print(f"The factorial of {f} is {product}")
# product = 1
# i = 1
# while i <= f:
#     product = product * i
#     i = i + 1
#     print(f"The factorial of {f}is{product}")

# Star Method


#   *
#  ***
# *****
n = int(input("Enter the star number!"))

for i in range(1,n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i- 1), end="" )
    print("")



# Factorial using Recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(f"The factorial of {n} is {factorial(5)}")


# hello


