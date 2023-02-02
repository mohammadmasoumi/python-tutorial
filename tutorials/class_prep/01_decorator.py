# keep the main function behaviour

import functools


def decorator1(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return res

    return wrapper

def decorator2(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return res

    return wrapper

@decorator1
def function1():
    pass

@decorator2
def function2():
    pass

print(function1)
print(function2)