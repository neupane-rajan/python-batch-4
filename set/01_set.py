# set: A set is an unordered collection of unique elements in Python.


# creating an empty set
empty1 = {}  # dict
empty = set()  # set
single_value = {1}  # set


# print(type(empty))

nums = {1, 2, 3, 4, 5, 6}
# print(type(nums))


# 1.unorder

nums = {1, 2, 3, 4, 5, 6}
# print(nums)

random_set = {"ball", 123, "hello", True, "i", "random", None}
# print(random_set)


# 2. unique: set remove duplicate value automatically
set1 = {"raj", "raj", 1, 2, 3, 4, 5, 1, 9, 4, 9, 0, 0, 1, 2, 1, 1, 1, 1, 1}
# print(set1)

# 3. mutable: we can change set after creating it.
messages = {"hello", "hi", "goodmorning"}
messages.add("good night")
# print(messages)


# accessing sets value

messages = {"hello", "hi", "goodmorning"}
# for message in messages:
#     print(message)


# checking membership(using in )(return true or false)

numbers = {10, 20, 30, 40, 50}

print(-20 in numbers)
