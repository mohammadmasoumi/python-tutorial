set1 = {1, 2, 3}
set2 = {2, 4, 5}

print("intersection اشتراک")
# set1 = set1.intersection(set2)
set3 = set1.intersection(set2)  # return a new set
print(set1)
# اشتراک را بدست آورده و در ست اول جایگزین میکند.
set1.intersection_update(set2)  # update the first one
print(set1)

print("union اجتماع")

set1 = {1, 2, 3}
set2 = {2, 4, 5}
# A U B
set4 = set1.union(set2)
print(set4)
# print(*set4) packing

# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(set1 + set2)

#
print("Difference ")
set1 = {1, 2, 3}
set2 = {2, 4, 5}

# A - B
# set1 - set2
print(set1.difference(set2))
# set2 - set1
print(set2.difference(set1))

set1.difference_update(set2)
print(set1)

# A U B - A ^ B
# دلتا
print("Symmetric difference")
set1 = {1, 2, 3}
set2 = {2, 4, 5}

set5 = set1.symmetric_difference(set2)
print(set3)
print(set2.symmetric_difference(set1))
set1.symmetric_difference_update(set2)
print(set1)
