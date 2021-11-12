a = input()
b = input()

diff = 0
"""
0123
aabb
01
aa
"""
for idx, item in enumerate(a):
    # print(a[idx], b[idx])
    # item: a, idx: 0
    print(f"[A]: idx: {idx}, item: {item}")
    if idx < len(b):  # 3 < 2
        print(f"[B]: idx: {idx}, item: {b[idx]}")
        if a[idx] != b[idx]:
            diff += 1
    else:
        diff += 1

print(f"diff: {diff}")
