"""
11 33
"""
h, l = input().split()
h, l = int(h), int(l)

for i in range((h - 1) // 2):
    print(("|*|" * ((2 * i) + 1)).center(l, '-'))

print("GeeksForGeeks".center(l, '-'))

for i in range(((h - 1) // 2) - 1, -1, -1):
    print(("|*|" * ((2 * i) + 1)).center(l, '-'))
