# error handling

"""
handle errors
keywords

[*] finally runs in anycase
"""

"""
1. if exception raised in try
2. run exception block
3. run finally 
"""

"""
1. if exception does not raise in try
2. run else block
3. run finally
"""

"""
External connection 

1. open file (close file in finally)
2. connect to db (close connection with db in finally)
3. ... 

"""


# try:
#     a = input()
#     print(int(a)) # raise ValueError
#     # print(int(a) // 0) # raise ZeroDivisionError
# except ValueError as asghar:
#     print("ValueError")
# except ZeroDivisionError as e:
#     print("ZeroDivisionError")
# else:
#     print("Else .....")
# finally:
#     print("Finally ...")

# print("Hello ...................")

"""
w -> write/override
r -> read
a -> append
"""

try:
    #           file_name file_mode
    file = open("file.txt", "a")
    int("ali")
except Exception as exc:
    print("Exception has been occured!")
    raise ValueError("ValueError")
else:
    for i in range(100):
        file.write(f"Welcome to the program {i}\n")
finally:
    file.close()
    print("Finally!")
    # ValueError: I/O operation on closed file.
    # file.write("Hello, ....")
