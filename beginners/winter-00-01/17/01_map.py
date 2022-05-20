# "12 13 14 15"
# ["12", "13", "14", "15"]
n = input().split()

# [12, 13, 14, 15]
for idx, item in enumerate(n):
    n[idx] = int(item)

# builtin function
# map(function, iterable)
# iterable: list

print(n)