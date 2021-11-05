a_tuple = (1, 2, 3, 4, 5)
# a_tuple.index()
# a_tuple.count()
# del a_tuple

# index
print(a_tuple[2:])
print(a_tuple[:2])
print(a_tuple[-3:-1])

#  in membership
if 1 in a_tuple:
    print("`1` is in a_tuple")

# immutable
s = "Hello"
# s = s + " World"
s += " World"
print(s)

# a_tuple = a_tuple + (1, 2, 3)
a_tuple += (1, 2, 3)
print(f"a_tuple: {a_tuple}")

# (1, 2, 3, 4, 5, 1, 2, 3) +  (1, 2, 3, 4, 5, 1, 2, 3)
# (1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3)
a_tuple *= 2
print(f"a_tuple: {a_tuple}")

# TypeError: unsupported operand type(s) for /=: 'tuple' and 'int'
# a_tuple /= 2
# print(f"a_tuple: {a_tuple}")

# TypeError: unsupported operand type(s) for -=: 'tuple' and 'tuple'
# a_tuple -= (1, 2, 3)
# print(f"a_tuple: {a_tuple}")
# (1, 2, 3, 4, 5, 6)
a_tuple1 = (1, 2, 3)
a_tuple2 = (4, 5, 6)
print((*a_tuple1, *a_tuple2))
