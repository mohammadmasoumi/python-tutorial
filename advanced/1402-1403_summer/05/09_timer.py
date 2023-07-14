import time

def timer(f):
    def wrapper(*args, **kwargs):
        s = time.perf_counter()
        res = f(*args, **kwargs)
        e = time.perf_counter()
        print(f"{f.__name__} has taken {e - s}s to run!")
        return res
    return wrapper


@timer
def add(a, b):
    for _ in range(10000000):
        pass
    return a + b


@timer
def multi(a, b):
    for _ in range(100000000):
        pass
    return a * b


add(10, 12)
multi(10, 12)
