set1 = {12, 13}
set2 = {12, 14}

# (set1 U set2)  - (set1 n set2)
# (12, 13, 14) - {12}
# there is no union update
symmetric_difference = set1.symmetric_difference(set2)
print(f"symmetric_difference: {symmetric_difference}")
print(f"set1: {set1}")
print(f"set2: {set2}")

# symmetric_difference = set1.symmetric_difference(set2)
# set1 = symmetric_difference

set1.symmetric_difference_update(set2)
print(f"set1: {set1}")
print(f"set2: {set2}")