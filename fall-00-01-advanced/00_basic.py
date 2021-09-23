import math
from math import sqrt

a = sqrt(16)
b = math.sqrt(16)

# select multiple line: shift + down arrow
# comment out multiple line ctrl + /
# a = 1
# b = 2

# follow PEP rules
# ctrl + a
# ctrl + alt + l

# https://www.python.org/dev/peps/
print("Hello world")  # no semi-colon

# debugger
# integer
# snake case
an_int1 = 1
an_int2 = 2

# string
# multiple comment
"""
My string
"""
a_string = "my string"

# float | double
a_float1 = 10.1
a_float2 = 10.1

# https://www.tutorialspoint.com/What-are-Reserved-Keywords-in-Python#:~:text=Python%20Server%20Side%20Programming%20Programming.%20Reserved%20words%20%28also,programming%20elements%20like%20name%20of%20variable%2C%20function%20etc.
# int
# char
# float

sum_of_int = an_int1 + an_int2
minus_of_int = an_int1 - an_int2
reminder = an_int1 % an_int2
multiple_of_float = a_float1 * a_float2
div_of_int1 = an_int1 / an_int2
div_of_int2 = an_int1 // an_int2  # round result
pow_an_int = 2 ** 10  # power

# an_int2 = 2
# Immutable
print(++an_int2)  # 3
print(an_int2 + 1)

# an_int2 = 2
print(an_int2)  # 2
# an_int2 = 3

an_int1 += 1
# f-string
print(f"an_int1: {an_int1}")

# input and output
# my_input = input()
my_input = ""
print("my_input: {my_input}")
print(f"my_input: {my_input}")

# boolean
a_true_boolean = True
a_false_boolean = False

# indentation
if a_true_boolean and a_false_boolean and a_false_boolean and a_false_boolean:
    print(f"And")

if a_false_boolean and a_true_boolean and a_true_boolean and a_true_boolean:
    print(f"And")


if a_true_boolean or a_false_boolean:
    print(f"Or")

# No xor
# if a_true_boolean xor a_false_boolean:
#     print(f"Or")


if a_true_boolean:
    print("a_true_boolean")

if a_false_boolean:
    print("a_false_boolean")

if not a_false_boolean:
    print("a_false_boolean")


