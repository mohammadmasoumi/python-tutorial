"""
bitwise
& | ^ ~

-----------------
logical
and
or
not


[True, False]
"""

print(f"True and True: {True and True}")

a = 0 and True
b = 12 and True
c = 0 and False
d = 12 and False

print(a, type(a))
print(b, type(b))
print(c, type(c))

print("==========================")
print(f"0 and True: {0 and True}")
print(f"0 or True: {0 or True}")
print(f"True and 0: {True and 0}")
print(f"True or 0: {True or 0}")
print("==========================")
print(f"0 and False: {0 and False}")
print(f"False and 0: {False and 0}")
print("==========================")
print(f"12 and True: {12 and True}")  # bool(12)
print(f"12 and False: {12 and False}")  # bool(0)
print("==========================")
print(f"1 and False: {1 and False}")
print(f"1 and True: {1 and True}")
print(f"1 or True: {1 or True}")
print(f"True or 1: {True or 1}")
print("==========================")

# دومی اصلا اجرا نمیشود.
print(True or 12 / 0)
print(False and 12 / 0)

# not
print("==========================")
print(not True)
print(not False)
print(not 0)
print(not 1)
print(not 12)  # bool(12) = True
