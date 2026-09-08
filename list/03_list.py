# list with loop

users = ["Uttam", "Rohit", "Rejina", "Ramit", "random"]
# print(users)


# for i in users:
#     print(type(i))


# list creation

list1 = list(range(1, 10))
name = "random"
name_list = list(name)
num = 123451  # we cannot convert integer into list.
# print(name_list)

# Membership testing
# in, not in (returns value either in True or False )

users = ["rohit", "uttam", "ramit", "rejina"]

# print("Rohit" in users)
# if "Rohit" in users:
#     print("user exist")


# len()
users = ["rohit", "uttam", "ramit", "rejina"]
# print(len(users))

# list unpacing
loan = [1, "rohit", 500]
# loan_id = loan[0]
# user = loan[1]
# loan_amount = loan[2]

loan_id, user, loan_amount = loan

# print(user)

# Extended unpacking
numbers = [1, 2, 3, 4, 5, 6]
first, *middle, last = numbers
print(f"first: {first}\nmiddle: {middle}\nlast:{last}")

