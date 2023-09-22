#
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# -----
# t1 = (1, 2, 3) + (10, 11, 12) merge tuples
# t1 = (1, 2, 3, 10, 11, 12)
# my_list = []
# for index in range(len(t1)):
#     value_t1 = t1[index]
#     value_t2 = t2[index]
#     my_list.append(value_t1 + value_t2)

"""
t1 -X-> (1, 2, 3) GC
 |----> (1, 2, 3, 10, 11, 12) 

t2 -> (10, 11, 12)
"""

# mutable
# my_list = []
# my_list.append(2)

# t1 -> (1, 2, 3)
# t1 -> (1, 2, 3, 10, 11, 12)
# t1 = t1 + t2
t3 = t1 + t2
t1 += (10, 11, 12)

a = 12
b = 13
c = a + b
# t1 = 12
print(t1)

"""
a -> 12
b -> 13
"""

# -----
a = 12
a += 1
print(a)

b = a
a += 1
# b # immutable
