# duplicate not allowed
# unordered
# changeable
set1 = {1, 2, 3}

# TypeError: 'set' object is not subscriptable
# you can not access to the set via index
# print(set1[0])

for item in set1:
    print(item)

print(1 in set1)
print(2 in set1)
print(3 in [1, 2, 3])
print(3 in (1, 2, 3))

# find an element in set
# if 3 in set1:
#     print()

# alternative find an element in set
# for item in [1, 2, 3]:
#     if item == 3:
#         # todo sth
#         break
