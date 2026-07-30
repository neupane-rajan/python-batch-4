# parameter: a parameter is a variable that receives data when the function is called
name = input("enter your name: ")
course = input("which language you want to learn: ")


def greeting(x, y, z):  # parameter
    print(
        f"hello {x}, thank you for joining {y} course.All the  best for your future{z}!"
    )


greeting(x=course,y=name,z="hello")  # argument
