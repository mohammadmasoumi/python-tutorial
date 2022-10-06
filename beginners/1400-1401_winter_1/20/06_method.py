A = {1, 2, 3}
B = {2, 3, 4}

# A - B 
# {1}
print(A.difference(B))
C = A.difference(B)
# B - A
# {4}
print(f"A:{A}, B: {B}")

# A = A - B
# A.difference_update(B)
# print(f"A:{A}, B: {B}")


# intersection
# A ^ B
print(A.intersection(B))
D = A.intersection(B)

# A.intersection_update(B)
# print(f"A:{A}, B: {B}")

# union
# A U B
print(A.union(B))
E = A.union(B)


# delta
# (A U B) - (A ^ B)
# A - B U B - A
print(A.symmetric_difference(B))

F = A.symmetric_difference(B)


