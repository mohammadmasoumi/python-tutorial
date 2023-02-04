a = 12
b = 13
c = 14

# 1.
temp = a
a = b
b = temp

# 2. 
a = a + b # a: 25, b: 13
b = a - b # b: 12, a: 25
a = a - b # a: 13, b: 12

# 3.
# unpacking
a, b = b, a

# ValueError: too many values to unpack (expected 2)
# a, b = b, a, c

# ValueError: not enough values to unpack (expected 3, got 2)
# a, b, c = b, a




