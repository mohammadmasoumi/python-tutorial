import time


def timer(func):

    def wrapper():
        s = time.perf_counter()
        func()
        e = time.perf_counter()
        print(f"{func.__name__}: {(e - s): .2f}")

    return wrapper


@timer
def long_method1():
    for _ in range(10000):
        pass

@timer
def long_method2():
    for _ in range(1000):
        pass

@timer
def long_method3():
    for _ in range(100000):
        pass

# s = time.perf_counter()
# long_method1()
# e = time.perf_counter()
# print(e - s)

long_method1()
long_method2()
long_method3()