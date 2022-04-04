# error handling 

"""
A
Traceback (most recent call last):
  File "c:/Users/MFT SERVER/Desktop/python/advanced-python2/11/04_error_handling.py", line 3, in <module>
    n = int(input())
ValueError: invalid literal for int() with base 10: 'A'
"""

# type: ValueError
# desciption: invalid literal for int() with base 10: 'A'
# "12" or "12"

"""
try, catch

keywords:
    try
    except

    else
    finally

1. a = int(input())
2. if raise exception
3. goto line 33 (except:)
4. print("invalid input")
   running = True

"""
running = True

while running:
    try:
        a = int(input())
        b = input("Do you wanna continue? (y/n)")

        if b == "y":
            running = True
        else:
            running = False
    except:
        print("Invalid input")
        running = True


# if isinstance(a, int):
#     print("Hello")

# if a and b == isinstance(a or b , int)
# if isinstance(a, int) or isinstance(b, int)


# print(f"result: {a}")

