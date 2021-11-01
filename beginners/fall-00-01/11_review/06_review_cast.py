# casting data-types
# int, float, bool, str, list
# type(variable)

asghar = 12

# 12asghar

# variable:
# name => asghar
# value => 12
# type => int 

# bool - keyword - [True, False]
true_var = True # bool(1, 2, 3 , .... -1, -2 , .... ) , bool(" ")
false_var = False # bool(0), bool(""), bool('')

# --------------------------
# int
a = 12
a_int = int(a)  # int -> int
a_float = float(a) # int -> float
a_bool = bool(a) # int -> bool 
a_false_bool = bool(0)
a_str = str(a)  # int -> str
# TypeError: 'int' object is not iterable
# a_list = list(a) # int -> list 

print(f"value: {a_int} - type: {type(a_int)}") # 12
print(f"value: {a_float} - type: {type(a_float)}") # 12.0
print(f"value: {a_bool} - type: {type(a_bool)}") # True
print(f"value: {a_false_bool} - type: {type(a_false_bool)}") # False
print(f"value: {a_str} - type: {type(a_str)}")  # "12" - '12'


# float


# str - "string" 'string'
b1 = "123"
b2 = "Hello"
b3 = "0"
b4 = "" # empty string
b5 = "Hello world"

b1_int = int(b1) # str -> int

# ValueError: invalid literal for int() with base 10: 'Hello'
#b2_int = int(b2) # str -> int
b1_float = float(b1) # str -> float
b1_bool = bool(b1) # str -> bool
b3_bool = bool(b3) # str -> bool
b4_bool = bool(b4) # str -> bool
b1_str = str(b1) # str -> str
b1_list = list(b1) # str -> list
b5_list = list(b5) # str -> list

print(f"value: {b1_int} - type: {type(b1_int)}") # 123
#print(f"value: {b2_int} - type: {type(b2_int)}")
print(f"value: {b1_float} - type: {type(b1_float)}") # 123.0
print(f"value: {b1_bool} - type: {type(b1_bool)}")  # True
print(f"value: {b3_bool} - type: {type(b3_bool)}") # True
print(f"value: {b4_bool} - type: {type(b4_bool)}") # False
print(f"value: {b4_bool} - type: {type(b4_bool)}") # False
print(f"value: {b1_str} - type: {type(b1_str)}") # "123"
print(f"value: {b1_list} - type: {type(b1_list)}") # ['1', '2', '3']
#  012345678910
# "Hello world" => ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(f"value: {b5_list} - type: {type(b5_list)}") 

# -----------------------------------------
my_name = "" # str

# if condition:
# condition -> True, False - bool
# bool(my_name)
# if bool(my_name):
# bool("") -> False
if my_name:
    print("My name is not empty")
else:
    print("My name is empty")
