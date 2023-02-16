# list

"""
Hold multiple values

 - index, indice
 - different type

# dynamic type
[1, "hello", True]
[1, 2, 3, 4]

a = []
a = "hello"

# immutable or mutable
[mutable]

# immutable
a = 12
a += 1 # a: 13

# ordered or unordered
[ordered0 => index, indice]

# duplication is allowed
[1, 1]

[list]
 - Changeable/mutable
 - Ordered => index
 - Allowed duplication

HOTEL
 0  1  2  3  4  5  6
[ ][ ][ ][ ][ ][ ][ ]

"""

# brackets
my_list = []  # empty list

# inital value
my_list = [1, 2, "hello"]
my_list = [1, 1.1, True, "hello", [1, 2]]

# 2D array
my_list = [[1, 2], [3, 4]]

# access to elem
# index, indice
print(my_list[0])  # my_list[0]: [1, 2]
# IndexError: list index out of range
# print(my_list[10])

# [1, 2] [1]
print(my_list[0][1])  # 2
print(my_list[1][0])  # 3

# typing
my_list: list = []
my_list: list[int] = [1, 2, 3]

print(my_list)

# update
my_list = [1, 2, 3]
print(my_list[1])  # READ
my_list[1] = 4
print(my_list)

# range => 0: 2
# IndexError: list assignment index out of range
# my_list[10] = 10

# delete a variable
# del my_list # delete a variable

# NameError: name 'my_list' is not defined
# print(my_list)

del my_list[1]
print(my_list)

my_list = ["mahdi", "foad", "amirhossein"]

# TypeError: list indices must be integers or slices, not str
# del my_list["amirhossein"]
del my_list[2]
print(my_list)

# IndexError: list assignment index out of range
# del my_list[2]
# print(my_list)
