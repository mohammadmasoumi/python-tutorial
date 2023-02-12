from functools import wraps
import tracemalloc
from time import perf_counter 

"""
See: https://www.freecodecamp.org/news/python-decorators-explained-with-examples/
"""

def measure_performance(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()

        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()

    return wrapper


@measure_performance
def make_list1():
    my_list = list(range(100000))


@measure_performance
def make_list2():
    my_list = [l for l in range(100000)]


@measure_performance
def make_list3():
    my_list = []
    for item in range(100000):
        my_list.append(item)


@measure_performance
def make_list4():
    my_list = []
    for item in range(100000):
        my_list = my_list + [item]


make_list1()
make_list2()
make_list3()
make_list4()