# methods of set

# without copy
set1 = {1, 2, 3, 4}
set2 = set1

set1.add(5)
print(set1, set2)

# with copy
set1 = {1, 2, 3, 4}
set2 = set1.copy()

set1.add(5)
print(set1, set2)

# disjoint
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}
set3 = {1, 3, 10}

# set1 ^ set2 = None
# set1.intersection(set2) = set() | {}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))

# issubset
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5}

# set1 ⊆ set2
print(set1.issubset(set2))
print(set2.issuperset(set1))

# clear
set1.clear()