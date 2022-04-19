# concatenation

a_tuple = (1, 2, 3, 3)
a1_tuple = (1, 2, 3, 3)

b_tuple = (4, 5, 6, 6)

c_tuple = a_tuple + a1_tuple

# ordered
ordered_tuple = b_tuple + a1_tuple

# print(c_tuple)
# print(ordered_tuple)

# create new tuple
single_tuple = (1,)
t1 = (1, 2, 3)
t2 = tuple(t1)
t3 = (*t1,)

print(t1)
print(t2)
print(t3)

l1 = [1, 2, 3]
l2 = [*l1]
print(l1)
print(l2)
