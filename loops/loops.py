"""
a loop is a programming structure that allow us to execute a block of code, multiple times.

range(end) :
range(start,end)
range(start,stop,step)
for i in range(5, -2, -1):
    print(i)

there are mainly 2 types of loop in python
for loop: used when we know how many times to repeat
while loop: used when we dont know exact count or i have certain condtion

"""

i = 1
while i <=5:
    print(i)
    i += 1  # i = i + 1

# print your name 5 times
i = 1
while i <=10:
    print("rajan")
    i = i+1 # i +=1


# infinite loop 

while True:
    print("hello")

    

