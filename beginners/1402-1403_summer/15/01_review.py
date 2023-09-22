t1 = (1, 1, 2, 3)

# Return first index of value.
# Raises ValueError if the value is not present.

#            0  1  2
# t1[1:] => (1, 2, 3)
print(t1[1:].index(1))  # 1: value

# slicing always create new list/tuple/string t1[1:]
print(t1[1:][2])  # 3
