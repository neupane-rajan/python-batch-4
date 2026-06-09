"""
for variable in sequence:
    code...

where,
for -> for loop lai define ganre keyword ho
variable -> jasma temporary value store garna sakinxa
# where squence = range(), string,list,tuple, dict, sets

"""

# in below example loop start from 0 and edn at 10 but 10 is not included in the loop
# for i in range(10):
#     print(i)

# for i in range(1,11):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# loop with string
# name = "niijo"
# for i in name:
#     print(i)

# name = "niijo"
# for i in range(len(name)):
#     print(name[i])


# loop with list
alphabet = ["a", "b", "c", "d", "e"]

# for i in alphabet:
#     print(i)


# loop with integer: we can not used loop on integer\

# loop with tuple:
# t = (1, 2, 3, 4, 5, 6)
# for i in t:
#     print(i)


# loop with sets
# set1 = {1, 2, 3, 4, 5, 6}
# for i in set1:
#     print(i)


# loop with dict

my_info = {"name": "Rajan", "age": 18, "address": "lamki"}

# for key,value in my_info.items():
#     print(key,value)



# reverse counting

for i in range(10,-1,-1):
    if i%2!=0:
        print(i)

