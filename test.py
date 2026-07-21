num = int(input("enter any number: "))

reverse = 0
temp = num
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print(num)
print(reverse)
if reverse == temp:
    print("number is a palindrome")
else:
    print("number is not a palindrome")
