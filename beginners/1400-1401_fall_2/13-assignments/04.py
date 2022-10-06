n = int(input())
width = 2 * n - 1 

for idx in range(n):
    print(("*" * (2 * idx + 1)).center(width))

for idx in range(n-2, -1, -1):
    print(("*" * (2 * idx + 1)).center(width))
