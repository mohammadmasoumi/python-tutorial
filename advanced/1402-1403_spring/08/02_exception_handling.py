# Exception handling

"""
raise

try:

except:

except:

else:

finally:

"""

# n = input()

# if n.isdigit():
#     n = int(n)

#     if n != 0:
#         print(12/n)

try:
    n = int(input())
    print(12/n)
    # raise ValueError()

except Exception as e: # ValueError, ZeroDivision
    # e: instance of exception
    print(e.with_traceback)
    print("I got string instead of int")

"""
Exception
ValueError
ZeroDivision
"""