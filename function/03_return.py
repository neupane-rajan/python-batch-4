# return holds value of function


def add(a, b):
    return a + b


sum = add(1, 3)
# print(sum)


def calculator(a, b):
    return a + b, a - b, a * b, a / b


# print(calculator(5, 4))
# sum, sub, mul, div = calculator(5, 2)

# print(sum)
# print(sub)
# print(mul)
# print(div)


def check_age(age):

    if age < 18:

        return "minor"

    return "adult"


# print(check_age(17))


# create a function that returns :
# square
# cube
# area of rectange
# largest among 3 number
# even or odd


# variable scope 
# global variable
# local variable


name = "Niijo"

def show():
    print(f"we are {name}")

# show()

def test():
    age = 18
    return age

test()
print(test())


