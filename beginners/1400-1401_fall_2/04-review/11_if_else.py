"""

if condition:
    # do sth

if condition:
    # do sth
else:
    # do sth else
"""
"""
Odd or Even

20

20 / 2 = 10, 0
5 / 2 = 2, 1

"""
a = int(input())

"""
a % 2 => [0, 1]

if 0: if False
if 1: if True

"""
# a = 12
if a % 2 == 0:
    print(f"{a} is Even!")

    # nested if
    if a == 12:
        print(f"{a} is equal to 12")

    print("End!")

else:
    print(f"{a} is Odd!")

# ------------------------
# if a:
if not (a % 2):
    print(f"{a} is Even!")
else:
    print(f"{a} is Odd!")

# ------------------------
# if 1:  # 1
#     print("1")

if a % 2:  # 1 bool(1) , bool(0)
    print(f"{a} is Odd!")
else:
    print(f"{a} is Even!")
