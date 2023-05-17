# anonymous function

"""
1. break down logic
500

- 10
- 10
- 10

2. reusable
"""

# function declaration


def my_func(x):
    # x: 10, x: 11
    x *= 2  # x: 20, x: 22
    x = x % 10  # x: 0, x: 2
    x *= 10  # x: 0, x: 20
    x /= 2  # x: 0, x: 10.0
    return x  # jump back to: 41, 44


# a = 12
# my_func: variable
# <function my_func at 0x0000023E20A2F0A0>
print(my_func)

"""
division:
    truediv -> //
    floordiv -> /
"""

# call, invoke
#
# | ---- ^
# v      |
num = my_func(10)  # Stop: -> jump to: 17
print(num)

num = my_func(11)  # Stop: -> jump to: 17
print(num)


# anonymous function
my_list = [1, 2, 3, 4, 5]

print(list(filter(lambda x: x % 2, my_list)))

# you do not have access to: lambda x: x % 2

# lambda inputs: output