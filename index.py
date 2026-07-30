from random import randint
import random
import math
import re
from functools import reduce
# import pyjokes

# variable = pyjokes.get_joke()

# print(variable)


a = 5
b = 10

print(a % b)



# a1 = 34
# b2 = 80

# print(a1>b2)

Name = "KRISH"

shortName = Name[0:3]

print(shortName)


# value = "Hey \" Krish\" what's going \n on did you finish your homework or not?"

# print(value)

# name = input("Enter your Name plz..")

# print(f"Hii My Handsome {name}")

word = "Krish"

print(word[1:6:2])


arry = ["krish",1,0.25,True,'Apple'];
# insert(index,element)
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




kk = ["Nikhil", "Akaansh", "Divyance", "pepsi", "KFC", "Sting"]

i = 0

while i < len(kk):
    print(kk[i])
    i += 1

print(len(kk))


numbers = [1,2,3,4,5,7,8,9,10]

for item in numbers:
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
# n = int(input("Enter the star number!"))


# for i in range(1,n + 1):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i- 1), end="" )
#     print("")



# for i in range(1,n + 1):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i- 1), end="" )
#     print("")

# Factorial using Recursion

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(f"The factorial of {n} is {factorial(5)}")

# Reverse Table..
# n = int(input("Enter the number:"))

# for i in range(1,11):
#     print(f"{n} X {11-i} = {n*(11-i)} ")

# # Function...
# def goodDay(name,ending):
#     print("Good Day,"+name)
#     print(ending)
#     return "ok"

# a = goodDay("Harry","Thank you")
# print(a)

# hello
# find the gratest of 3 numbers


# testing 

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))

# def greatest(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     elif c>=b and c>=a:
#         return c
# print(f"The greatest number is {greatest(a,b,c)}")


# print("a",end="")
# print("b",end="")
# print("c",end="")

# sum
# def sum(n):
#     if n == 1:
#         return 1
#     else: 
#         return sum(n-1) + n
     
# man = int(input("Enter the value: "))

# print(sum(man))


# a = ["House","of","ballon"]

# i = 0
# while  i< len(a):
#     print("Loop value: ",a[i])
#     i += 1


# PRACTISE SET-9
# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.

with open("poem.txt") as f:
    text = f.read()

if "twinkle" in text.lower():
    print("The word 'twinkle' is present in the file.")
else:
    print("The word 'twinkle' is not present in the file.")


with open("starboy.txt") as a:
    text = a.read()

    if "we don't pray for love, we just pray for cars" in text.lower():
        print("THE WORD IS PRESENT!..")
    else:
        print("THE WORLD IS NOT PRESENT..!")

# The game() function in a program lets a user play a game and return the score as an integer. you need to read a file 'Hi-score.txt' which is either blank or contains the previousHi-Score. You need to write a program to update the Hi-score whenever the game() function bracks the Hi-score..

def game():
    print("You are playing the game..:")

    score = random.randint(1, 62)
    # Fetch hiScore 
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score:{score}")

    if score > hiscore:
        # write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
 

#  Write a program to generate multiplication tables from 2 to 20 and write it to the different files. place these files in a folder for a 13 years_old_child..

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n}X{i}={n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for n in range(2, 21):
    generateTable(n)



word = "donkey"



with open("file.txt","r") as f:
    content = f.read()

contentNew = re.sub(word, "#####", content, flags=re.IGNORECASE)

with open("file.txt", "w")as f:
    f.write(contentNew)


# OBJECT ORITENTED PROGRAMMING....


class Employee:
    name = "Harry"
    language = "python"
    salary= 1200000


# dunder method in python...
    def __init__(self,name,language,salary):
     self.name= name
     self.salary = salary
     self.language = language
     print("I am creating an obeject...!")

    def getinfo(self):
     print(f"The language is {self.language}. The salary is {self.salary}")


krish = Employee("Krish",140000,"Javascrit")    
krish.getinfo()

# PRACTISE SET CHAPTER 10...
#1. Create a class "PRogrammer" for storing information of few programmers working at microsoft...
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
      self.name =  name
      self.salary = salary
      self.pin = pin


p = Programmer("Harry",120000,24005)
print(p.name,p.salary,p.pin,p.company)

# 2. Write a class "calculator" capable of finding square, cube and square root of a number.
class calculater:
    def __init__(self,n):
        self.n = n
    
    def square(self):
     print(f"The Square is {self.n*self.n}")

    def cube(self):
     print(f"The Cube is {self.n*self.n*self.n}")

    def squareRoot(self):
      print(f"The SquareRoot is {math.sqrt(self.n)}")
a = calculater(2)

a.square()
a.cube()
a.squareRoot()


# def sq(n):
#    fn = n*n
#    print(f"The square value {fn}")


# sq(16)

# Write a class train which has methods to book a ticket, get status(no of seats) and get fare information of train running under Indian Railways

# class Train:
    
#     def __init__(self, trainNo):
#         self.trainNo = trainNo

#     def book(self, fro, to):
#         print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")   
    
#     def getStatus(self):
#         print(f"Train no: {self.trainNo} is running on time")

#     def getFare(self, fro, to):
#         print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")    

# t = Train(12399)

# t.book("Rampur","Delhi")
   
# t.getStatus()
   
# t.getFare("rampur","Delhi")
    
# Inheritance
class Employee:
    company= "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "ITC Infotect" 
    
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company,b.company)

class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

e1 = Employee("Krish")
e2 = Employee("Rahul")

e1.company = "Microsoft"

print(e1.company)
print(e2.company)
print(Employee.company)


# multilevel_inheritance

class student:
    a = 1
class marks(student):
    b = 2
class subjects(student):
    c = 3

o = student()
print(o.a)

o = marks()
print(o.a,o.b)

o = subjects()
print(o.a,o.c)

# Class Method
# A class method is a method which bound to the class and not the object of the class.
# @classmethod
# class  Employee:
#     a = 1

#     @classmethod
#     def show(cls):
#         print(f"The class attribute of a is {cls.a}")

# e = Employee()

# e.a = 45

# e.show()

# Property_decorator

class Employee:
    def __init__(self):
        self.salary = 40000
        self.bonus = 10000

    def total_salary(self):
     return self.salary + self.bonus

e = Employee()
print(e.total_salary())  # Output: 50000   

# With property decorator we can access the method as an attribute without using ().

class Employee:
    def __init__(self):
        self.salary = 40000
        self.bonus = 10000

    @property
    def total_salary(self):
        return self.salary + self.bonus
e = Employee()
print(e.total_salary)


# Practise Set Chapter 11

# Create a class (2-D Vector) and use it to create class representing a 3-D vector.

class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i+{self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i+{self.j}j+{self.k}k")    

a = TwoDVector(2,3)
a.show()
b = ThreeDVector(1,2,3)
b.show()

# 2 Create a Class 'pets' form a class "Animal" and futher create a class "Dog" from "pets". Add a Method "bark" to class 'Dog"
class Animal:
  pass

class Pets(Animal):
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print("Woof Woof!")

d = Dog()
d.bark()        

# 3 create a class 'Employee' and add salary and increment properties to it..
# Write a method "salaryAfterIncrement" method with a @property decorator with a setter which changes the value of increment based on the salary...
class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100


e = Employee()
print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 280.8
print(e.increment)

# Wrtie a class 'complex' to represent complex numbers, along with overloaded operations "+" and "*" operator which calculates the sum nd the dot(.) product of them....

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        # Return a new instance of Complex, not Python's built-in complex
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)  # Output: 4 + 6i
print(c1 * c2)  # Output: -5 + 10i


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
while (users := fetch_user_batch(page)):
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

while (users := fetcher.fetch_user_batch()):
        print(f"Processing page {fetcher.page - 1}: {users}") 

# Types Definition in python:
age: int = 25 

def greeting(name: str) ->str:
    return f"Hiiiiiiiiiiiiiiiiii,{name}"
print(greeting("Radha...."))
# TRY or Exception

# try: 
#     a = int(input("ENTER THE NUMBER..."))
#     print(a)

# except Exception as e:
#     print(e)    

# print("still working....")

# def fb():
#     try:
#         n = int(input("Enter the number: "))
#     except ValueError:
#         print("Please enter a valid number.")
#         return

#     if n % 2 == 0:
#         print("EVEN NUMBER")
#     else:
#         print("ODD NUMBER")

# fb()

# Chapter 13 

square = lambda x:x*x

print(square(6))

name = ["Krish" ,"Love" ,"BMW" ,"sports" ,"Cars"]

output = "_".join(name)

print(output)

# Formate String Method
a = "{} is a smart guy in the domain of {}".format("krish","Computer_science.")
print(a)

# Map , Fliter Reduce:
# map() applies a function to every item in an iterable and returns a map object. It is commonly used to transform data without writing an explicit loop.


def CovertIntoCapital(ab):
    return ab.upper()

ab = ["krish", "rahul", "aman"]

FinalOutput = list(map(CovertIntoCapital,ab))

print(FinalOutput)



# Without using a for loop, use map() to convert:   
# Without using a for loop, use map() to convert:



def only_names(student):
    return student.get("name").capitalize()

students = [
    {"name": "krish", "marks": 80},
    {"name": "rahul", "marks": 65},
    {"name": "aman", "marks": 90},
    {"name": "rahul", "marks":40}
]

result = list(map(only_names, students))

print(result)

# Fliters
L = [1,2,3,4,5,6,7]
def even(n):
    if(n%2 ==00):
        return True
    return False

onlyEven = filter(even,L)
print(list(onlyEven))


# Fliters
def passed(student):
    return student["marks"] >= 80

result = list(filter(passed, students))

print(result)
# Reduce Example:
def sum(a,b):
     return a + b
output = reduce(sum,L)

print(output)


# Find the largest number Without using sum()


numbers = [12, 56, 23, 98, 45]

def largest(x, y):
    if x > y:
        return x
    else:
        return y

output = reduce(largest, numbers)

print(output)
# Pracrise SET...
table = [str(3*i) for i in range(1,11)]

s = "\n".join(table)
print(s)

# Find the Greatest Number...

num = [1,2,3,4,50,6,7,10]

def FindNum(a,b):
    if(a>b):
        return a
    return b

outCome = reduce(FindNum,num)
print(f"Greater Number is {outCome}")
