# string arithmetic

#         012345678910
string = "hello world"

# string[1]
print(string[0] * 10)
print("h" * 10)
# "hhhhhhhhhh"

# a list with one element
# repeation
my_list = [1, 2] * 10
# [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(my_list)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# TypeError: unsupported operand type(s) for /: 'str' and 'int'
# print(string[0] / 10)
# TypeError: can only concatenate str (not "int") to str
# print(string[0] + 10)
# TypeError: unsupported operand type(s) for -: 'str' and 'int'
# print(string[0] - 10)

my_string1 = "hello" "world"
print(f"my_string1: {my_string1}")
my_string2 = (
    "hello" 
    "world"
)
print(f"my_string2: {my_string2}")
