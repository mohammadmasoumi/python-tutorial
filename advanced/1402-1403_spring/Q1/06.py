import time
import functools


def timer(f):

    @functools.wraps(f)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        res = f(*args, **kwargs)
        end_time = time.perf_counter()

        print(f"Finished {f.__name__!r} in {end_time - start_time:.4f} secs")
        
        return res

    return wrapper_timer

@timer
def f1():
    for _ in range(100000):
        pass

@timer
def f2():
    for _ in range(1000000):
        pass


f1()
f2()