# Comparison operator
# عملگرهای مقایسه

"""
>
<
==
!=
>= (> or ==)
<= (< or ==)

Output: Boolean
"""
# int
print(12 < 13)  # True
print(12 <= 13)  # 12 < 13 or 12 == 13
print(12 >= 13)  # False
print(12 == 12)
print(12 != 13)  # True

# float
print(12.2 < 13)  # True

# str
# len
#      10 > 3 X
#
# "yaalimadad"
# "ali"
print("yaalimadad" > "ali")

# ASCII CODE
# @
# .
# A: 65
# B: 66
#
# a: 97
# b: 98
# c: 99
# ...
# ali 97
# Ali 65
print("Ali" < "ali")

# z
# bbbbbbbbbbbbbbbbbbbbbbbbb
print("z" > "b" * 100)

# aab
# ab
print("aab" < "ab")


# "ab**2" > "ab**3"
# "ab**2"
# "ab**3"
print("ab**2" > "ab**3")
