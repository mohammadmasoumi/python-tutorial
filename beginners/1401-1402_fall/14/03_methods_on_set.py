set1 = {1, 2, 3}
set2 = {2, 3}
set3 = {4, 5}
set4 = {2, 5, 6}
set5 = {1, 2, 5, 6}
#
print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set1.isdisjoint(set3))

#
# set1 - set2
diff_set1_set2 = set1.difference(set2)
# set2 - set1
diff_set2_set1 = set2.difference(set1)

print(diff_set1_set2)
print(diff_set2_set1)

# set1 = set1.difference(set2)
# Remove all elements of another set from this set.
# set1.difference_update(set2)
# print(set1)
# set2.difference_update(set1)

# set1 U set2
union_set1_set2 = set1.union(set2)
# union_set2_set1 = set2.union(set1)
print(union_set1_set2)

# set1 ^ set2
intersection_set1_set2 = set1.intersection(set2)
print(union_set1_set2)

# set1.intersection_update(set2)
# print(set1)
# set2.intersection_update(set1)
# print(set2)

# a - b U b - a
print(set1.symmetric_difference(set5))

# set1.symmetric_difference_update(set5)
# set5.symmetric_difference_update(set1)
