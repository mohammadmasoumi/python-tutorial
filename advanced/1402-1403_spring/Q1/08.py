import functools
import time

"""
See: https://realpython.com/primer-on-python-decorators/
"""
def slow_down(f):
    
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        time.sleep(1)
        return f(*args, **kwargs)
    
    return wrapper

@slow_down
def f1():
    print("Hello")

for _ in range(10):
    f1()