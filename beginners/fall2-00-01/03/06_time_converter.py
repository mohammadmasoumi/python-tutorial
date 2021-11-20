# time converter

# user interaction
number = int(input("Enter time(hour): "))
# number = input("Enter time(hour): ")
# number = int(number)

"""
fog => f(g(x))

b = int(input())
a = input()
b = int(a)
"""

# str + str -> str
# a + b -> ab

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(number * 3600 + "seconds")  # int + str - raise exception
# print(str(number * 3600) + " seconds")  # str(int) + str
# print(number * 3600, "seconds", sep="-")


#          str / int raise exception
#          str + int raise exception
print(f"{number * 3600} seconds")
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
print(f"{number / 60} minutes")
