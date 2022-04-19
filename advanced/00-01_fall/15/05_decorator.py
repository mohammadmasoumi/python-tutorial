import time


def timer(func):
    def wrapper(*args, **kwargs):
        # time.time()
        t1 = time.perf_counter()
        func(*args, **kwargs)
        t2 = time.perf_counter()

        diff = t2 - t1
        print(f"t2: {t2}, t1: {t1}, {diff} seconds, {diff * 1000} miliseconds")

    return wrapper


@timer
def test(n):
    # n * 2
    # for _ in range(n):
    #     pass
    # for _ in range(n):
    #     pass

    # n ** 2
    for _ in range(n):
        for _ in range(n):
            pass


test(100)
test(1000)
test(10000)
# test(100000)
# from time import time
# https://www.epochconverter.com/
# print(time.time())
