a = {"apple", "orange", "banana", "peach", "carrot"}  # {1, 2, 5}
b = {"apple", "orange", "watermelon", "pineapple", "cucumber", "cherry"}

# eshterak - intersection
c = a.intersection(b)

# a = a.intersection(b)
# a.intersection_update(b)

# b = a.intersection(b)
# b.intersection_update(a)

print(f"a intersection b: {c}")
# print(f"a intersection b: {a}")
# print(f"a intersection b: {b}")

# ejtemae - union

d = a.union(b)
print(f"a union b: {d}")

# difference - ekhtelaf

# A - B
f = a.difference(b)
g = b.difference(a)

# a = = a.difference(b)
a.difference_update(b)
# b = = b.difference(a)
b.difference_update(a)

print(f"a difference b: {f}")
print(f"b difference a: {g}")

# delta - symmetric difference
# روی رشته ها کار نمیکند
a1 = {1, 2, 3}
b1 = {2, 4, 5}

print(a1.symmetric_difference(b1))
# a1 = a1.symmetric_difference(b1)
a1.symmetric_difference_update(b1)
print(a1)

# does not work on strings
k = b.symmetric_difference(a)
# a.symmetric_difference_update(b)
print(f"a symmetric_difference b: {k}")
