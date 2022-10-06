#          -8  -7   -6   -5     -4     -3       -2      -1
#           0  1     2    3      4      5        6       7
a_tuple = (1, "A", 12.9, True, False, None, [1, 2, 3], [1, 2])

print(f"a_tuple: {a_tuple}")

# solution 1
for i in a_tuple:
    # type(i) == list
    if isinstance(i, list):
        i.append(4)

# solution 2
print(a_tuple[-2])
print(a_tuple[6])
a_tuple[-2].append(5)
a_tuple[6].append(10)
print(a_tuple)

