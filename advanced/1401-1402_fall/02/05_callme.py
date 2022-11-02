import time

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def minus(a, b):
    return a - b

# ctrl + shift + l
def timer(f, a, b):
    s = time.perf_counter()
    result =  f(a, b)
    e = time.perf_counter()

    print(f"time: {e - s}")

    return result

# 1
s = time.perf_counter()
print(add(10, 12))
e = time.perf_counter()
print(f"time: {e - s}")

s = time.perf_counter()
print(minus(10, 12))
e = time.perf_counter()
print(f"time: {e - s}")

# 2
print(timer(add, 10, 12))
print("-------------------------")

def logger(f, a, b):
    print(f"Calling {f.__name__} function with {a} and {b}.")
    result =  f(a, b)
    print(f"Result {result}.")

    return result

logger(add, 10, 12)

# 3
print("-------------------------")

def run_twice(f, a, b):
    f(a, b)
    return f(a, b)


run_twice(add, 10, 12)