# Nested if
# sometimes we use if inside another if (nested if)
"""
# syntax
if condition:
    if condition:
        statement
"""

"""
# example 1

print("-----------------------------vote eligibility checker-----------------")

age = int(input("enter your age"))
check_citizen = input("are you  Nepali citizen(y/n)")

if age >=18:
    if check_citizen=="y":
        print("you can vote")
    else:
        print("you are not from nepal")
else:
    print("you are not young enough to vote")

"""

#example 2

# program to check whether a given number is postive even number or not

num = int(input("enter a number to check: "))

if num >=0:
    if num%2==0:
        print("number is positive even number!")
    else:
        print("number is postive odd number")

else:

    print("number is negative")
    

    