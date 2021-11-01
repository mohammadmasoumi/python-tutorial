#          0 ---- len(my_list) -1
#  index   0  1  2  3
my_list = [1, 2, 3, 4]
print(f"len: {len(my_list)}")
print(f"type: {type(my_list)}")

# unpacking
#    0  1
m = [1, 2]

# give me the value of room 0
#a = m[0] 
#b = m[1]

# a, b = [1, 2]
a, b = m
print(f"a: {a} - b: {b}")

# ValueError: too many values to unpack (expected 2)
# a1, b1 = [1, 2, 3]
a1, b1, c1 = [1, 2, 3]
print(f"a1: {a1} - b1: {b1} - c1: {c1}")

# 
a3, *b3 = [1, 2, 3, 4]
print(f"a3: {a3}, b3: {b3}")

# ValueError: not enough values to unpack (expected 3, got 2)
# a2, b2, c2 = [1, 2]
a2, b2, c2 = [1, 2, 3]
print(f"a2: {a2} - b2: {b2} - c2: {c2}")
