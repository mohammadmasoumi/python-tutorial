
# timer
# logger
# log into files
# times

import functools  
  
class Count_Calls:  
    def __init__(self, func):  
        functools.update_wrapper(self, func)  
        self.func = func  
        self.num_calls = 0  
  
    def __call__(self, *args, **kwargs):  
        self.num_calls += 1  
        print(f"Call{self.num_calls} of {self.func.__name__!r}")  
        return self.func(*args, **kwargs)  

from functools import wraps
import tracemalloc
from time import perf_counter 


def measure_performance(func):
    '''Measure performance of a function'''

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
    '''Range'''

    my_list = list(range(100000))


@measure_performance
def make_list2():
    '''List comprehension'''

    my_list = [l for l in range(100000)]


@measure_performance
def make_list3():
    '''Append'''

    my_list = []
    for item in range(100000):
        my_list.append(item)


@measure_performance
def make_list4():
    '''Concatenation'''

    my_list = []
    for item in range(100000):
        my_list = my_list + [item]