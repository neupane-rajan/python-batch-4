"""
sequence: a list of numbers arranged in a particular order.
 example: 1, 2, 3, 4, 5, 6, 7
series: sum of sequence or numbers
example: 1+2+3+4+5=15

"""

#  print number from 1 to 20

# for i in range(1,11):
#     print(i,end=" ")
# output: 1 2 3 4 5 6 7 8 9 10


# print number from 10 to 1

# for i in range(10,0,-1):
#     print(i, end=" ")

# print sequence of even number to 30
# for i in range(1, 31):
#     if i % 2 == 0:
#         print(i)

# print sequence of odd number to 30
# for i in range(1, 31):
#     if i % 2 != 0:
#         print(i)


# sequence
total = 0
for i in range(1, 21):
    total = total + i
print(total)