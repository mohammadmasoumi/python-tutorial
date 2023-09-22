# intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

intersection = set1.intersection(set2)
print(f"intersection: {intersection} | set1: {set1} | set2: {set2}")

# ctrl + / (slash)
# \ back slash
set1.intersection_update(set2)
# set1 = set1.intersection(set2)
print(f"set1: {set1} | set2: {set2}")

set2.intersection_update(set1)
# set1 = set1.intersection(set2)
print(f"set1: {set1} | set2: {set2}")

# union
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

union = set1.union(set2)
print(f"union: {union}")
# no union_update

# symmetric_difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# set1 delta set2
# A U B - A ^ B
# {1, 2, 3, 6, 7}
symmetric_difference = set1.symmetric_difference(set2)
print(f"symmetric_difference: {symmetric_difference}")
# set1.symmetric_difference_update(set2)

# difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

d1 = set1.difference(set2)  # set1 - set2: {1, 2, 3} | set1 - (set1 ^ set2)
d2 = set2.difference(set1)  # set2 - set1: {6, 7} | set2 - (set1 ^ set2)

print(f"d1: {d1} | d2: {d2}")
print(f"delta: {d1.union(d2)}")  # symmetric_difference
