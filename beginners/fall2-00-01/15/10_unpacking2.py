# a, b, c = [1, 2]

# ValueError: not enough values to unpack (expected 3, got 2)
for a, b, c in [[1, 2], [4, 5, 6]]:
    print(f"a: {a}, b: {b}, c: {c}")
