# error handling

"""
handle errors
keywords
"""

try:
    a = input()
    print(int(a)) # raise ValueError
    print(int(a) // 0) # raise ZeroDivisionError
except ValueError as asghar:
    print("ValueError")
    # print("ZeroDivisionError")
    # print(asghar)
    print(type(asghar))
    # raise asghar
    # raise ValueError("Sorry, There is an exception in program!")
except ZeroDivisionError as e:
    print("ZeroDivisionError")
    

print("Hello .......")