# if we have multiple condition then we use elif

"""
syntax:
if condition:
    statement
elif condition:
    statement
elif condtoin:
    statement
    .........
    .........
else:
    statement

# esle is optional
"""
# find greates among two number

num1 = int(input("enter your first number: "))
num2 = int(input("enter you second number: "))

if num1>num2:
    print(f"{num1} is greatest")
elif num2>num1:
    print(f"{num2} is greatest")
# elif num1==num2:
#     print("both are equal")
else:
    print("both are equal")




# 