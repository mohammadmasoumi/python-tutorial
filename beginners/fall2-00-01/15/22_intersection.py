set1 = {12, 13}
set2 = {12, 14}

# set1 n set2
intersection = set1.intersection(set2)
print(f"intersection: {intersection}")
print(f"set1: {set1}")
print(f"set2: {set2}")

# intersection = set1.intersection(set2)
# set1 = intersection

set1.intersection_update(set2)
print(f"set1: {set1}")
print(f"set2: {set2}")