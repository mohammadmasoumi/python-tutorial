a, b = 12, 13
a1, b1 = (12, 13)

print(a, b)

for item in enumerate([1, 2, 3]):
    print(item, type(item))

for idx, elem in enumerate([1, 2, 3]):
    print(f"idx: {idx}, elem: {elem}")

for item in [[1, 2, 3], [4, 5, 6]]:
    a, b, c = item
    print(f"item: {item}, a: {a}, b: {b}, c: {c}")

for a, b, c in [[1, 2, 3], [4, 5, 6]]:
    print(f"a: {a}, b: {b}, c: {c}")
