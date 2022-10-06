set1 = {12, 13}
set2 = {12, 14}

# set1 - set2
diff1 = set1.difference(set2)
print(f"diff1: {diff1}")
print(f"set1: {set1}")
print(f"set2: {set2}")

# diff1 = set1.difference(set2)
# set1 = diff1

# set1 = set1 - set2
set1.difference_update(set2)
print(f"set1: {set1}")
print(f"set2: {set2}")