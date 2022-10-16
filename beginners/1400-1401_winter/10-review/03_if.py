# if

"""
if condition and/or condiction and/or ...:

1.
if condition:
    # if-body
    # code block
    pass

2.
if condition:
    pass
else:
    pass

3.
if condition:
    pass
elif condition:
    pass
elif condition:
    pass
else:
    pass

# -----------------------------------
1.
if condition1:
    pass
if condition2:
    pass

2.
if condition1:
    pass
elif condition2:
    pass
"""

from distutils.command.config import config


condition = 12
if condition: # bool(condition)
    print("Condition is True!")
else:
    print("Condition is False!")

condition = 0
if condition:
    print("Condition is True!")
else:
    print("Condition is False!")

condition = 2
if condition == 2:
    print("Condition is 2")
else:
    print("Condition is not 2")

if condition <= 2:
    print("Condition <= 2")
elif 2 < condition <=5:
    print("2 < Condition <=5")
else:
    print("Condition > 5")

# Trick
true_condition = True
false_condition = False

# ZeroDivisionError: division by zero
# print(12 / 0)
if false_condition and 12 / 0:
    print("[AND] If the first condition is False, python does not care about second condition!")

if true_condition or 12 / 0:
    print("[OR] If the first condition is True, python does not care about second condition!")
