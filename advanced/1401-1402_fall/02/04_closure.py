# Closure
# bind a varialbe to a function 
import time

def multiplier(x):
    # x = 3

    def multiply(y):
        # y = 4
        return x * y

    return multiply

"""
def multiply1(y):
    # y = 4
    return 3 * y

def multiply2(y):
    # y = 4
    return 4 * y
"""

# multiply_by_3 = multiply
multiply_by_3 = multiplier(3)
print(multiply_by_3(4))
print(multiply_by_3(5))
print(multiply_by_3(100))

multiply_by_4 = multiplier(4)
print(multiply_by_4(4))

print("----------------------------------")
def print_msg(msg):
    # msg: "Hello"

    def printer():
        print(msg)

    return printer

# <function print_msg.<locals>.printer at 0x000001FDAD9F0550>
# print(print_msg("Hello"))

print_msg("Hello")()

p = print_msg("Hello")
p()

# [decorator]

# def timer(f):
    
#     def wrapper():
#         s = time.perf_counter()
#         r = f()
#         e = time.perf_counter()
#         print(e - s)
#         return r 
    
#     return wrapper 

# @timer
# def long_function():
#     for i in range(10000):
#         pass

# long_function()

# @timer
# def slow_function():
#     for i in range(10):
#         pass
        