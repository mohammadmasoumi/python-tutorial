# Selection statement

"""
and or not

if bool(condition and condition or ...):
    print("hello")

if not condition1:
    if condition2:
        print()

    print("Hello")

if condition1 and condition2:
    print()


if not                 (not(condition1 and condition2) or condition3):
    print("hello")

[Indentation]

if condition1:
  print("hello")
    print("hello")
else:
    print("")


if not(not(condition1 and condition2) or condition3 and condition4) and \
    not(not(condition1 and condition2) or condition3 and condition4):


if condition1:
    # if body
    print("hello")
else:
    # else body
    print("Bye")


if condition1:
    print("hello")
else:
    if condition2: 
        print("hello")
    else:
        if condition3:
            print("hello")


if condition1 and ...:
    print("hello")
elif condition2: 
    print("hello")
elif condition3:
    print("hello")
else:
    print("Bye")


if condition1:
    print("hello")
if condition2: 
    print("hello")
if condition3:
    print("hello")
else:
    print("Bye")


name = "Asghar"
last_name = ""

if name.startswith("A"):
    last_name = "Asghari"
else:
    last_name = "Akbari"


[Inline if-else]

variable_name = [TRUE VALUE] if [CONDITION] else [FALSE VALUE]
last_name = "Asghari" if name.startswith("A") else "Akbari"
"""
name = "Asghar"

if name.startswith("A"):
    last_name = "Asghari"
else:
    last_name = "Akbari"


# [Inline if-else]
# variable_name = [TRUE VALUE] if [CONDITION] else [FALSE VALUE]
last_name = "Asghari" if name.startswith("A") else "Akbari"
last_name = "Asghari" if name.startswith("A") else None

