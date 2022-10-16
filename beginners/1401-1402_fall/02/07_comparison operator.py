# Comparison operator

"""
>
<
>=
<=
==
!=
"""

print(12 > 13)

# "12"
# "2"
print("12" > "2")
print("2" > "12")

# ascii code
# ali
# hassan
print("ali" > "hassan")
print("ali" > "Hassan")

print(True == 1)

# TypeError: '>' not supported between instances of 'str' and 'int'
# print("ali" > 2)
print("ali" > "2")
print("ali" > "22222222222222222")
print("A" > "0")
print(12.0 > 12)
print(12.0 == 12)
print(12.0 >= 12)
print(12.3 > 12)
print("12.3" > "12")
print("12.0" > "12")

print(ord('a'), ord('2'), ord('A'))