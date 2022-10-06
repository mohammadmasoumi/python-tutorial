# fstring

# 1 - int

# 09
a = 9

print(f"{a}")

# colon :
# print(f"{a : 02}")
print(f"{a :02}")
print(f"{a :03}")

# - - - -
# - - - 9
# 0 0 0 9
print(f"{a :04}")

# 13 spaces + 9
#              9
print(f"{a :14}")

b = 123232
print(f"{b: 7}")

print("============================================")
# ------------------------------------------
# 2 - str

c = "abc"

# - - a b c
# >

print(f"{c: >5}")

# a b c - -
# <
print(f"{c: <5}")

print("============================================")
# ------------------------------------------

# 3 - float

d = 12.218943624823
print(f"{d:.2f}")
print(f"{d: .3f}")
print(f"{d:  .4f}")
# print(f"{d:   .4f}") ValueError: Invalid format specifier
