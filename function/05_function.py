# higher-order functions
# A function that accepts another function or returns another function is higher-order function


def greet():
    return "Hello"


def process(func):
    return func()


print(process(greet))


"""
# map:

map(function, iterables)
iterables: list,string,dict,range,tuple,set
when we try to print our map result it will give use memory address of map. if we want to see actual value then we have to convert it into either in list , tuple,set
"""


# def square(x):
#     return x**2


numbers = [1, 2, 3, 4, 5]

# result = map(square, numbers)
# print(list(result))

# using lambda function

result = map(lambda x: x**2, numbers)
print(list(result))

# convert name to uppercase
# convert strings to integer
# convert celsius to fahrenheit
# calculate squall of all given number(list)