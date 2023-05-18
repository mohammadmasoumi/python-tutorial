# methods of set
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# eshterak
# set1 ^ set2
print(set1.intersection(set2))

# ejtemae
# set1 U set2
print(set1.union(set2))

# ekhtelaf
# set1 - set2
# set2 - set1
print(set1.difference(set2))
print(set2.difference(set1))

# delta
# set1 - set2 U set2 - set1
print(set1.symmetric_difference(set2))

