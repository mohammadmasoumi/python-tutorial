
# timer
# logger
# log into files
# times
# register
# Slowing Down Code
# not during the night

# both
# def repeat(_func=None, *, num_times=2):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper_repeat

#     if _func is None:
#         return decorator_repeat
#     else:
#         return decorator_repeat(_func)


# import functools

# def singleton(cls):
#     """Make a class a Singleton class (only one instance)"""
#     @functools.wraps(cls)
#     def wrapper_singleton(*args, **kwargs):
#         if not wrapper_singleton.instance:
#             wrapper_singleton.instance = cls(*args, **kwargs)
#         return wrapper_singleton.instance
#     wrapper_singleton.instance = None
#     return wrapper_singleton

# @singleton
# class TheOne:
#     pass

# pass a function as argument
# return a function as a value 
# make prerry
# Who Are You, Really?
# Put simply: decorators wrap a function, modifying its behavior.

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = my_decorator(say_whee)

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


import requests


class LimitQuery:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.limit = args[0]
        if self.count < self.limit:
            self.count += 1
            return self.func(*args, **kwargs)
        else:
            print(f'No queries left. All {self.count} queries used.')
            return

@LimitQuery
def get_coin_price(limit):
    '''View the Bitcoin Price Index (BPI)'''
    
    url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    if url.status_code == 200:
        text = url.json()
        return f"${float(text['bpi']['USD']['rate_float']):.2f}"


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)


# import functools
# from decorators import count_calls

# def cache(func):
#     """Keep a cache of previous function calls"""
#     @functools.wraps(func)
#     def wrapper_cache(*args, **kwargs):
#         cache_key = args + tuple(kwargs.items())
#         if cache_key not in wrapper_cache.cache:
#             wrapper_cache.cache[cache_key] = func(*args, **kwargs)
#         return wrapper_cache.cache[cache_key]
#     wrapper_cache.cache = dict()
#     return wrapper_cache

# @cache
# @count_calls
# def fibonacci(num):
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)

# https://realpython.com/primer-on-python-decorators/