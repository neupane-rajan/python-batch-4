# list: A list is a container that allows ut to store multiple values in one variable.List is denoted by "[]"
# list are mutable
# user1 = "Uttam"
# user2 = "rohit"
# user3 = "rejina"
# user4 = "ramit"
# list allows us to store mutliple values with different data types
# in list python uses zero-based  indexing ( index number starts from 0)


random = [
    "abc",  # --> 0 index
    123,  # -->1 index
    1.1,  # --> 2 index ..so on
    None,
    True,
    3j,
    [1, 2, 3],
    {},  # --> -3 ...so on
    {1, 2, 3},  # --> -2
    (1, 2, 3),  # --> -1
]

# List Indexing
# print(random)
users = ["Uttam", "Rohit", "Rejina", "Ramit"]  # string list

# print(users)
# print(type(users))

users = ["Uttam", "Rohit", "Rejina", "..", ".............................", "Ramit"]

# print(users[1])
# print(users[3])
# print(users[-1])

# list slicing
# list_name[start:end]
# note: end is not included.
users = ["Uttam", "Rohit", "Rejina", "Ramit", "random"]

new_list = users[0:2]
# print(new_list)
# print(users[:]) #slice whole list
# print(users[0:5:2])
# print(users[::-1])


# practice 1


loans = [1000, 10000, 354300, 97234, 7037490327]
# first loan
# last  loan
# second loan
# first three loans
# last two loans

# Modifying lists
users = ["Uttam", "Rohit", "Rejina", "Ramit", "random"]

users[1] = "Ram"
print(users)

