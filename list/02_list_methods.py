"""List method"""

# append
# add something to the end

users = ["Uttam", "Rohit", "Rejina", "Ramit", "random"]
print(users)
users.append("jagdish")
# print(users)

# extend()
users = ["Uttam", "Rohit", "Rejina", "Ramit", "random"]
users.extend("xyz")
print(users)

# insert()
# Insert value at a particular index or position.

users = ["Uttam", "Rohit", "Rejina", "Ramit", "random"]
users.insert(1, "ramesh")

# print(users)

# remove()
# remove a specific value
users = ["Uttam", "Rohit", "Rejina", "Ramit", "random"]
# users.remove("random")
# print(users)

# pop()
# remove item using index number, in index is not given then it will remove last item of the  list.
users = ["Uttam", "Rohit", "Rejina", "Ramit", "random"]

users.pop(0)
print(users)
