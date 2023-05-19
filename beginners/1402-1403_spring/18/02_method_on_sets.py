"""
Set:
 - Duplication is NOT allowed
 - Mutable
 - Iterable
 - Unordered -> no index
 - All elements must be hashable
"""

my_set = set()

# intersection
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"intersection: {set1.intersection(set2)}")

set1.intersection_update(set2)
# set1 = set1.intersection(set2)

set2.intersection_update(set1)
# set2 = set1.intersection(set2)

print(f"set1: {set1}")
print(f"set2: {set2}")

print("------------------------")
# union
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"union: {set1.union(set2)}")
print(f"set1: {set1}")
print(f"set2: {set2}")

print("------------------------")
# difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"difference: {set1.difference(set2)}")
print(f"difference: {set2.difference(set1)}")

set1.difference_update(set2)
# set1 = set1.difference(set2)

set2.difference_update(set1)
# set2 = set2.difference(set1)

print(f"set1: {set1}")
print(f"set2: {set2}")

print("------------------------")
# symmetric difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# set1 U set2 - set1 ∩ set2
print(f"symmetric difference: {set1.symmetric_difference(set2)}")
print(f"symmetric difference: {set2.symmetric_difference(set1)}")

set1.symmetric_difference_update(set2)
# set1 = set1.symmetric_difference(set2)

set2.symmetric_difference_update(set1)
# set2 = set2.symmetric_difference(set1)

print(f"set1: {set1}")
print(f"set2: {set2}")
