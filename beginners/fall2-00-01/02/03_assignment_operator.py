"""


"""

a = 12
b = 14

# a = a + 12
# a = a + 12

# مقدار متغیر a را با 12 جمع کن و دوباره در متغیر a ذخیره کن
a += 12
print(f"{a}+= 12: {a}")
a -= 12
print(f"{a}-= 12: {a}")
a *= 12
print(f"{a}*= 12: {a}")
a /= 12
print(f"{a}/= 12: {a}")
a **= 12
print(f"{a}**= 12: {a}")
a //= 12
print(f"{a}//= 12: {a}")

"""
Bitwise operator
&
^
|
"""
print(f"5 & 7 = {5 & 7}")  # and
print(f"5 | 7 = {5 | 7}")  # or
print(f"5 ^ 7 = {5 ^ 7}")  # xor
print(f"~7 = {~7}")  # not

a = int(a)
# TypeError: unsupported operand type(s) for &=: 'float' and 'int'
a &= 12
print(f"{a}&= 12: {a}")

a |= 12
print(f"{a}|= 12: {a}")

a ^= 12
print(f"{a}^= 12: {a}")
