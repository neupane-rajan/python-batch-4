"""
while loop: A while loop repeatedly execute a block of code as long as a condition is True.


sytax:

while condition:
    code
"""

a = 1

# while a <= 5:
#     print(a)
#     a = a + 1

# infinite loop
# while True:
#     print("hello")


# count = 1
# while count>=1:
#     print(count)
#     count = count + 1


# stopping an infinite loop

# while True:
#     text = input("type e to exit: ")

#     if text == "e":
#         break


# continue: skips the current iteration

# count = 0
# while count <10:
#     count +=1
#     if count == 5:
#         continue
#     print(count)


# taking user input in while loop

# password = ""

# while password != "1234":
#     password = input("enter a password: ")

# print("Access Granted")


# number guessing game

# secret_number = 19
# guess = 0

# while guess != secret_number:
#     guess = int(input("guess the number: "))

# print("Correct")

# bomb using while loop
# count = 10

# while count > 0:
#     print(count)
#     count -= 1

# print("boooom!!")

# num = int(input("enter any number: "))

# i = 1

# while i<=10:
#     print(f"{num} x {i} = {num*i}")
#     i+=1


# while loop with else


count = 1

while count<=3:
    print(count)
    count+=1

else:
    print("loop finished")