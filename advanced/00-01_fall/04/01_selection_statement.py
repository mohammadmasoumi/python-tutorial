"""
keyword: if

if condition1 and condition2 and ...:
    # body if
    # code
    # code

print("Finish")
"""

a_condition = True

if a_condition:
    print("Hello if")

if 2:
    print("Hello 2")

# should have a condition
# if :

# if should have a body
# if a_condition:
#     pass

a = ""
if a:
    print("Hello")

b = 0
# b = "0"
if b:
    print("Hello")

# implicit casting
# bool(condition)
# if 2 * 2:
if 2 * 2 != 5:
    print("2*2 != 5")

# ! reverse
if not a_condition:
    print("")

# -----------------------------------------------------------------------
a_condition2 = 12
# b = bool(int(input()))
# b = bool(input())
# b = int(input())
b = False

# bool("0") is True
if b:
    print(f"{b} is True")
    print(f"{b} is True")
    print(f"{b} is True")
    print(f"{b} is True")
else:
    print(f"{b} is False")
    print(f"{b} is False")
    print(f"{b} is False")
    print(f"{b} is False")
    print(f"{b} is False")

# one else
# else:
#     print("Hello")
# if not a_condition2:
#     # pass
#     print("a_condition2 is False")
# else:
#     # pass
#     print("a_condition2 is True")

# -----------------------------------------------------------------------

# c = bool(int(input("Please enter a boolean: ")))
c = False
# inline if
# a_variable = result is True if condition else result is False
# d = "True" if c == "a" else "False"
d = "True" if c == True else "False"
print(f"d is: {d}")

# c2 = int(input())
# if c2 == 12:
#     print("cc2 is 12")

user_input = input()

if user_input == "A":
    print("A")
# else if -> elif
elif user_input == "B":
    print("B")
elif user_input == "C":
    print("C")
else:
    print(user_input)
