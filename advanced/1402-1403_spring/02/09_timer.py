import time

def timer(f):
    def wrapper(*args, **kwargs):
        # args = (12, 13)
        s = time.perf_counter()
        # f(*args)
        # f(*(12, 13)) => f(12, 13)
        # f(**{"a": 12, "b": 13}) => f(a=12, b=13)
        # print()
        res = f(*args, **kwargs)
        # print()
        e = time.perf_counter()
        print(f"latency: {e - s}")
        return res
        # return f(*args, **kwargs)
    return wrapper

@timer
def f1(n):
    for i in range(n):
        pass

@timer
def f2(n):
    for i in range(n):
        pass

@timer
def f3(n):
    for i in range(n):
        pass


f1(10000000)
f1(10000)
f1(100)

# print(f1(12, 13))
# w = logger(f1)
# print(w(12, 13))
