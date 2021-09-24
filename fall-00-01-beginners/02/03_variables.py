# readability
# description - doc
# do not execute

# name: a
# value: 2
# #2231 | --------- |
# #2232 |     2     |
# #2232 |           |
# #2232 | --------- |

# data-type
# integer

a = 2
a1 = int(2)
b = 3
c = 4

print(a)
print(b)
print(c)

# string
name1 = "ali"
name12 = str("ali")
name2 = "hossein"

print(name1)
print(name2)

# float
float1 = 12.1
float12 = float(12.1)
float2 = 14.9

print(float1)
print(float2)

# boolean - bool
a_false = False
a_false1 = bool(False)
# NameError: name 'false' is not defined
# a_false = false
a_true = True

print("---------------------------")
# ctrl + /
# put # on the first line
# print("Hello, world")

# dynamic type
# variable declare
# get variable type

a_dynamic_type = 10
print(type(a_dynamic_type))
a_dynamic_type = "Hello"
print(type(a_dynamic_type))
a_dynamic_type = 12.2
print(type(a_dynamic_type))
a_dynamic_type = True
print(type(a_dynamic_type))

print(a_dynamic_type)
print(type(a_dynamic_type))
print("---------------------------")

# cast
string12 = "12"
an_int1 = int("12")  # str -> int
an_int2 = int(string12)
an_int3 = int(12.9)  # float -> int
an_int4 = int('12')  # str -> int
an_int5 = int(True)  # bool -> int
an_int6 = int(False)  # bool -> int

print(an_int1)
print(an_int2)
print(an_int3)
print(an_int4)
print(an_int5)
print(an_int6)

# ascii
print(ord('a'))
print(ord('A'))
print(ord('.'))

# casting

# int -> str
my_string1 = str(12)
my_string3 = str(12500)

# float -> str
my_string2 = str(12.9)

# bool -> str
my_string4 = str(True)

print(my_string1)
print(type(my_string1))
print(my_string3)
print(type(my_string3))
print(my_string2)
print(type(my_string2))
print(my_string4)
print(type(my_string4))

# float

# int -> float
a_float1 = float(12)
a_float2 = float('12')
a_float3 = float(True)
a_float4 = float(False)

print(a_float1)
print(a_float2)
print(a_float3)
print(a_float4)

# bool

# int -> bool
a_bool1 = bool(12)
a_bool2 = bool(-12)
a_bool3 = bool(0)

print(a_bool1)
print(a_bool2)
print(a_bool3)

# str -> bool
a_bool4 = bool("ali")
a_bool5 = bool("")  # empty is False

print(a_bool4)
print(a_bool5)

# float -> bool
a_bool6 = bool(12.4)
a_bool7 = bool(0.4)
a_bool8 = bool(0.0)

print(a_bool6)
print(a_bool7)
print(a_bool8)

# single quote and double quotes

a_string1 = "ali"
a_string2 = str("ali")
a_string3 = 'ali'
a_string4 = str('ali')

# case sensitive
a = 12
A = 13

print(a)
print(A)
