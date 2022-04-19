# error handling

"""
handle errors
keywords

"""

try:
    a = input()
    print(int(a)) # raise ValueError
    print(int(a) // 0) # raise ZeroDivisionError

except (ValueError, ZeroDivisionError) as asghar:
    if isinstance(asghar, ValueError):
        print("ValueError")
    elif isinstance(asghar, ZeroDivisionError):
        print("ZeroDivisionError")
    
    # print(asghar)
    print(type(asghar))
    # raise asghar
    # raise ValueError("Sorry, There is an exception in program!")

print("Hello .......")