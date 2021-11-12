a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(a)
print(b)

c = a.symmetric_difference(b)
print(f"a=symmetric_difference: {c}")

print("___________________________________________")

d = a.union(b)
print(f"a.union: {d}")

print("___________________________________________")

e = a.intersection(b)
print(f"a=intersection: {e}")

print("___________________________________________")

f = a.difference(b)
print(f"a=difference: {f}")

print("___________________________________________")
