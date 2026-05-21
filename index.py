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