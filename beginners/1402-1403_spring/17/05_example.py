t1 = ({1, 2, 3, 4}, (1, 2), [1, 2, 3])

# type(t1[0]) -> set
t1[0].add(5)
print(t1)

# immutable
# TypeError: 'tuple' object does not support item assignment
# t1[1] += (2, 3)

# t2 = (1, 2)
# t2 += (3, 4)
# t1[1] = t2
# print(t2)

t1[2].append(5)
print(t1)

# TypeError: unhashable type: 'list'
# all elements of the set must be hashable
# 
# s1 = {[1, 2]}

# WRONG 
#  - hashable
#  - no index
# s1[0].append()

#        0       1
l1 = [(1, 2), (3, 4)]
l1[0] += (3, 4)

print(l1)

item = (1, 2)
t3 = ({1, 2, 3, 4}, item, [1, 2, 3])

item += (3, 4)
print(t3)
print(item)

print(t3[1])
print(id(t3[1]))
print(id(item))