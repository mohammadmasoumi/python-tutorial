# Count all decorated function's calls
import functools
from collections import defaultdict


# SOLUTION 1
def call_count(f):
    call_count.count = 0
    print("Called")

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        call_count.count += 1
        print(f"{f.__name__} called {call_count.count}")
        return f(*args, **kwargs)
    
    return wrapper

@call_count
def f1():
    pass

@call_count
def f2():
    pass

for _ in range(3):
    f1()
    f2()


# SOLUTION 2
"""
Count each decorated function's call separately

Set attribute dynamically for function
 - setattr(obj, attr, value) <=> obj.attr = value
 - getattr(obj, attr) <=> obj.attr

when to use?
    attribute name is dynamic and you have to create it.
"""

def count_each_function_call(f):
    # attribute name: {function_name}_count
    setattr(count_each_function_call, f"{f.__name__}_count", 0)
    print("Called")

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        count_so_far = getattr(count_each_function_call, f"{f.__name__}_count")
        count_so_far += 1

        # set new value
        setattr(count_each_function_call, f"{f.__name__}_count", count_so_far)
        print(f"{f.__name__} called {count_so_far}")

        return f(*args, **kwargs)
    
    return wrapper

@count_each_function_call
def f1():
    pass

@count_each_function_call
def f2():
    pass

for _ in range(3):
    f1()
    f2()


# SOLUTION 3
"""
defaultdict 

See: https://docs.python.org/3/library/collections.html#defaultdict-objects

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(sorted(d.items()))
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
"""

function_calls = defaultdict(int)

def count_each_function_call(f):

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        function_calls[f.__name__] += 1
        print(f"{f.__name__} called {function_calls[f.__name__]}")

        return f(*args, **kwargs)
    
    return wrapper

@count_each_function_call
def f1():
    pass

@count_each_function_call
def f2():
    pass

for _ in range(3):
    f1()
    f2()