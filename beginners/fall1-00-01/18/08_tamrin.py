# a = {1, 2, 3}  # set
# b = {'a': 1}  # dict


a = {1, 2, 3}
b = {3, 4, 5}

#  unsupported operand type(s) for +: 'set' and 'set'
# print(a + b)
print(a | b)  # union
print(a & b)  # intersection
print(a ^ b)  # symmetric difference

c = a.union(b)
d = a.intersection(b)
e = a.symmetric_difference(b)

print(c)
print(d)
print(e)

print((a | b) == (a.union(b)))
