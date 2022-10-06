import time

def logging(func):

    def wrapper(*args, **kwargs):
        args_str = " - ".join(map(str, args))
        kwargs_str = " - ".join([f"{k}:{v}" for k, v in kwargs.items()])
        
        print(f"args: {args_str} | kwargs: {kwargs_str}")
        return func(*args, **kwargs)

    return wrapper


def timer(func):

    def wrapper(*args, **kwargs):
        s1 = time.perf_counter()
        res = func(*args, **kwargs)
        s2 = time.perf_counter()

        print(f"Duration: {s2 - s1}")

        return res

    return wrapper

@logging
@timer
def my_sum(a, b):
    return a + b


my_sum(10, 20)