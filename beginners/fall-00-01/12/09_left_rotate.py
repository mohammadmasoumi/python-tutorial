"""
5 4
1 2 3 4 5
"""
n, rotate_count = input().split()
s = input().split()

rotate_count = int(rotate_count) % int(n)
print(s[rotate_count:] + s[:rotate_count])
