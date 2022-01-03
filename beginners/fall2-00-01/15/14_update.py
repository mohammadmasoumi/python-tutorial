my_tuple1 = ([12, 13], 12, 13)

# you can change element, if an element is mutable
my_tuple1[0].append(14)
my_tuple1[0].insert(1, 15)

# a = tuple(my_tuple1[0])
# print(a + (12, 13))

# you can not change the type of one lement
# my_tuple1[0] = tuple(my_tuple1[0])

print(my_tuple1)
print(type(my_tuple1))