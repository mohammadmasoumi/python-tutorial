# Decorator
import time


def timer(f):

    def wrapper():
        # 2022-10-29 20:05:04:123
        s = time.perf_counter()
        # long_function1()
        res = f()
        # 2022-10-29 20:05:05:123
        e = time.perf_counter()
        print(f"Duration: {e - s}")

        return res

    return wrapper

# wrapper = timer(long_function1)
# print(wrapper())


@timer
def long_function1():
    s = 0
    for item in range(100000):
        s += item

    return s


def long_function2():
    s = 0
    for item in range(1000000):
        s += item

    return s


# timer(long_function1)
# timer(long_function2)

print(long_function1())
