# higher-order functions
# A function that accepts another function or returns another function is higher-order function


def greet():
    return "Hello"


def process(func):
    return func()


# print(process(greet))


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
# print(list(result))

# convert names to uppercase
# convert strings to integer
# convert celsius to fahrenheit
# calculate squall of all given number(list)

names = ["ram", "shyam", "hari", "sita"]

up_result = map(lambda name: name.upper(), names)

# print(list(up_result))


# filter()
# filter(function, iterable)
numbers = [1, 2, 3, 4, 5, 6, 7]


# with filter
result = filter(lambda x: x % 2 == 0, numbers)

# print(list(result))

list[1, 2, 3, 4, 5, 6, 7, 8]
# even numbers
# odd numbers
# passed students
# positive numbers

# reduce


from functools import reduce

numbers = [1, 2, 3, 4, 5]
# here below a is function as result of a,b and b is next element(item)
result = reduce(lambda a, b: a + b, numbers)

print(result)
from functools import reduce

prices = []

# initial  value is given when we have empty list,dict , set  .... etc
total_purchase = reduce(lambda total, price: total + price, prices, 0)

print(total_purchase)


# map-> transform
# filter-> select(selective)
# reduce -> combine ->single value(result)