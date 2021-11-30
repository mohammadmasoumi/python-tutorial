"""
mark
A
B
C
D

A => 20
B => 19
C => 18
D => 17
"""

mark = input()

# mark = 'D'
# mark = 'A'

# 1
# Check all conditions in every occasion
if mark == 'A':
    print(f"mark is {20}")

if mark == 'B':
    print(f"mark is {19}")

if mark == 'C':
    print(f"mark is {18}")

if mark == 'D':
    print(f"mark is {17}")

# -------------------------------------------------
# 2
# mark = 'C'
"""
Invalid
Invalid
Invalid
mark is 17
"""

#
if mark == 'A':
    print(f"mark is {20}")
else:
    print("Invalid")

#
if mark == 'B':
    print(f"mark is {19}")
else:
    print("Invalid")

#
if mark == 'C':
    print(f"mark is {18}")
else:
    print("Invalid")

#
if mark == 'D':
    print(f"mark is {17}")
else:
    print("Invalid")

# 3

if mark == 'A':
    print(f"mark is {20}")
else:
    if mark == 'B':
        print(f"mark is {19}")
    else:
        if mark == 'C':
            print(f"mark is {18}")
        else:
            if mark == 'D':
                print(f"mark is {18}")

# 4

# elif => else if

# if condition:
# elif condition:
# else:


if mark == 'A':
    print(f"mark is {20}")
elif mark == 'B':
    print(f"mark is {19}")
elif mark == 'C':
    print(f"mark is {18}")
elif mark == 'D':
    print(f"mark is {17}")
else:
    print(f"Invalid!")
