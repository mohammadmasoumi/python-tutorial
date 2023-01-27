# 0, 1, 1, 2, 3, 5, 8, ...
n = int(input())

def fibo(m, direction="main"):
    if m == 1:
        return 0
    elif m == 2:
        return 1
    else:
        print(f"fibo({m}, {direction}) = fibo({m-2}, {direction}) + fibo({m-1}, {direction})")
        return fibo(m-2, "left") + fibo(m-1, "right")

print(fibo(n))

# n: 5
"""
          fibo(3) 1
    fibo(2)     fibo(1)
        1           0

"""

def factorial(m):
    if m == 1:
        return 1

    return m * factorial(m-1)

print(factorial(5))