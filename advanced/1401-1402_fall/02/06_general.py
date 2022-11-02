import time

def add(a, b):
    return a + b

def multiply(a, b, c):
    return a * b * c

def minus(a, b):
    return a - b

# positional argument
multiply(12, 13, 14)
multiply(12, 14, 13)

# key word argument
multiply(a=12, c=14, b=13)
multiply(c=12, a=14, b=13)


def timer(f, *args):
    s = time.perf_counter()
    result =  f(*args)
    e = time.perf_counter()

    print(f"time: {e - s}")

    return result

print(timer(add, 10, 12))
print(timer(multiply, 10, 12, 14))
