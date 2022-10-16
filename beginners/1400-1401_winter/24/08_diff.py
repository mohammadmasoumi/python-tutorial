
a = input()
b = input()

"""
aab
aa
diff: 1

a
bcd
diff: 3
"""
diff = 0

for idx in range(min(len(a), len(b))):
    if a[idx] != b[idx]:
        diff += 1

diff += abs(len(a) - len(b))

# diff = sum([1 for idx in range(min(len(a), len(b))) if a[idx] != b[idx] ]) + abs(len(a) - len(b))
print(diff)