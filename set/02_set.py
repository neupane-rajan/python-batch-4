# update(): update() adds multiple elements from another iterable to a set
# set,tuple,list range,string,dict

nums = {1, 2, 3}
nums.update(["a", "b", "c", None])
nums.update("hello")
# print(nums)

# remove(): remove an element from a set and rasie KeyError if the element doesn't exist in the set.

# nums.remove("h")

# nums.remove("-1")
# print(nums)


# discard: remove an element froma a set and doesnt raise any error if element is not present in set.

# nums.discard(-1)

letters = {"a", "b", "c", "d"}
# pop()
# print(letters.pop())
# print(letters)


# clear()
nums = {1,2,3,4,5}
nums.clear()
print(nums)

# 