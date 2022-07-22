# error handling

"""
handle errors
keywords
"""

try:
    a = input()
    print(int(a)) # raise ValueError
    # print(int(a) // 0) # raise ZeroDivisionError
except ValueError as asghar:
    print("ValueError")
except ZeroDivisionError as e:
    print("ZeroDivisionError")
else:
    print("Hello .....")
