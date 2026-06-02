name = "nepal"
# print(type(name))


# string indexing
new_string = "helloworld"
# h   e   l   l   o   w   o   r   l   d
# 0   1   2   3   4   5   6   7   8   9 # positive indexing
# -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 # negative indexing

# print(new_string[0])
# print(new_string[-2])


# string slicing

# hobby = "programming"
# # new_slice = hobby[0:4]
# # print(new_slice)
# print(hobby[:4])  # -> [0:4] == [:4]
# print(hobby[4:])  # start from 4th index goes up to end of the string
# print(hobby[4:4]) # no output here
# print(hobby[:]) # whole string


# step slicing

# [a:b:c]
# where a = startng point(included), b= ending point [excluded],c = how many step to jump
test = "programming"

# print(test[::3])
# print(test[::-1]) # reverse the string

# print(test[1:6:2])



# string concatenation
# joining string together

first_word = "hello"
second_word = "world"

new_word = first_word + " " + second_word
# print(new_word)
first_name = "rajan "
second_name = "neupane"
full_name = first_name + second_name
# print(full_name)


# string repetitoin

rep_string = "hi"*4
# print(rep_string)

# membership operators
# check whether something exists in a string or not

sentence = "I am python from  tech"

# print("am" in sentence)



# string methods

# upper() : make all the letter to uppercase
name = "ramesh"
print(name.upper())

# lower()


# len() : give length of the string

xyz = "hellodlkahflkdhjalkhfdlkhalkdfhdjlajfdl;jlkadjfl;kjdlk;afjlksdj"
print(len(xyz))