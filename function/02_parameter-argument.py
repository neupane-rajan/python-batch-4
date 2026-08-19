# parameter: a parameter is a variable that receives data when the function is called
# name = input("enter your name: ")
# course = input("which language you want to learn: ")


def greeting(x, y, z):  # parameter
    print(
        f"hello {x}, thank you for joining {y} course.All the  best for your future{z}!"
    )


# greeting(x=course,y=name,z="hello")  # argument


# advance paremeter,

# default paremeter


def greet(name="guest"):  # default argument
    print(f"hello {name} welcome to niijo tech")


# greet()
# greet(name="rahul")

# *args : accept multiple arguments


def new_fucntion(*num):
    return num


x = new_fucntion(1, 2, 3, 4, 5)
# print(type(x))

# example


def total(*nums):
    sum = 0

    for i in nums:
        sum += i
    return sum


# print(total(1, 2, 3, 4, 5, 6))


# **kwargs


def mart_bill(**details):

    for item, price in details.items():
        print(f"{item}: {price}")


mart_bill(coke=21, penutbutter=450, xtereme=140, Ramen=250)
