# Type conversion/ Type casting
# changing  one data type into another data type is called type conversion


# integer to string

# int_num = 123

# new_num = str(int_num)
# print(new_num)
# print(type(new_num))

# string to integer

new_str = "123"
converted_str = int(new_str)
# print(type(converted_str))

# note: only integer number  type(combination  of number from 0 to 9) string can be converted into integer
# my_name = "rajan"
# new_int = int(my_name)
# print(new_int)
# print(type(new_int))

# lenght = "99.99"
#  new_length= int(length)
# print(type(new_length))

# string to float : fraction number 1.2 type and integer number type string can be converted into float
# price = "99.9"
# new_price = float(price)
# print(type(new_price))

# float to int ( only take number before "." and exclude the number after ".")
# frac_num = 2.9
# int_num = int(frac_num)
# print(int_num)
# print(type(int_num))


# converting other data types into boolean

# string to boolean
# if we convert non-empty string into boolean, it will be converted into True
# if the string is empty and it will be converted into False
new_str = ""
into_bool = bool(new_str)
# print(into_bool)

# integer to boolean
# all things except 0 is converted into integer.
new_int = 0
into_bool = bool(new_int)
print(into_bool)
