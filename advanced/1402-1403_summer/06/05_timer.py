import time

def timer(f):

    def wrapper(*args, **kwargs):
        s = time.perf_counter()
        res = f(*args, **kwargs)
        e = time.perf_counter()

        # f.__name__: time_consuming_function
        print(f"{f.__name__} executed in {e - s}ms.")
        return res 

    return wrapper

@timer
def time_consuming_function():
    for _ in range(100000):
        pass


time_consuming_function()

