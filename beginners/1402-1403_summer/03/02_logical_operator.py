# Logical operator

"""
or  ||
and &&
not !

Combination

condition1
condition2
condition3

condition1 and condition2

c1: The weather is great
c2: The car is healthy

c1 and c2 -> go to Tehran

AND DECISTION TABLE
c1    c2    r
True  True  True  
False False False
False True  False
True  False False

-------------
c1 and c2 and c3 => True
All the conditions are True
-------------
OR DECISTION TABLE
c1    c2    r
True  True  True  
False False False
False True  True
True  False True

Boolean??
"""

is_even = True
is_odd = False

# ---------
print(is_even and is_odd)
#   c1: bool and c2: bool
# c1 and c2
print(True and True)
# True
#      bool and int
print(True and 12)  # True: 2, error: 1,

# True -> return the last value
# [True and True] and True and "Hello"
# True and True => True
# [True and True] and "Hello"
# True and True => True
# True and "Hello"
# "Hello"

print(True and True and True and "Hello")
# False -> False
# اگر همه شرطها درست باشد آخرین متغیر یا مقدار را برمیگرداند
# اگر حداقل یک شرط غلط باشد فالس بر میگردد
# logical operator -> return the last one or False

# --------------

a = 12
b = 0

#       False      True     ZeroDivisionException
print(b != 0 and a != 0 and a / b)  # False

# if b != 0:
#     print(a / b)

# AND
# if a condition is False, the final result is False
# > it won't check other conditions

# OR
# if a condition is True, the final result is True
# > it won't check other conditions

# python java
# and    &&
# or     ||
# not    !
