import functools
from collections import defaultdict


def call_count(f):
    call_count.count = {}
    # call_count.count = defaultdict(int)
    print("Called")

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        exists = call_count.count.get(f.__name__)
        if exists:
            call_count.count[f.__name__] += 1
        else:
            call_count.count[f.__name__] = 1
        
        # call_count.count[f.__name__] += 1

        print(f"{f.__name__} called {call_count.count[f.__name__]}")

        return f(*args, **kwargs)

    return wrapper


@call_count
def f1():
    pass


@call_count
def f2():
    pass


f1()
f1()
f1()

f2()
f2()
f2()
