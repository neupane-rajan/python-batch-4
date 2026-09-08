# list comprehensions
# variable_name = [operation]

numbers = [1, 2, 3, 4, 5, 6, 7]

square = []

for number in numbers:
    square.append(number * number)
print(square)

squares = ["hello" for i in number]

print(squares)

for i in number:
    print("hello")

numbers = [1, 2, 3, 4, 5, 6, 7]
even_num = [num for num in numbers if num % 2 == 0]

even_num = []
for num in numbers:
    if num % 2 == 0:
        even_num.append(num)

