# input() when we use input for taking data from user then by default they have string data type .if you want that data in integer then we can use int() method for converting it into integer
# f-string: f-string is a way of formatting string in python . It is a new way to formate string and it is more redable and concise way to formate a string.
# we can use f-string by adding f before the quote ("") and using curly braces{ } to insert variables into string


num1 = int(input("enter you first number"))
num2 = int(input("enter second number"))
# print(type(num1), type(num2))
# print(num1 + num2)

name = "rajan"
age = 21
# print("hello my name is", name, " i am", age, "years old")

print(f"hello my name is {name}. I am {age} years old . ")


# name,school ,age, address
# Hello I am Rajan. I am 21 years old. My school name is niijo_academy.I live in lamki

name = input("name: ")
age = input("age: ")
school = input("school: ")
address = input("address: ")

print(
    f"Hello I am {name}. I am {age} years old. My school name is {school}. I live in {address}"
)
