# decorator
import functools

def decorator(f):
    # state 
    # decorated function
    call_count = 0
    called_with_args = {}

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        nonlocal call_count, called_with_args
        call_count += 1
        
        res = f(*args, **kwargs)
        called_with_args[hash(args)] = res

        print(f"{f.__name__} has called {call_count} times.")
        print(f"called_with_args: {called_with_args}")
        return res

    return wrapper


# wrapper = decorator(add)
@decorator
def add(a, b):
    return a + b

@decorator
def mul(a, b):
    return a * b


add(10, 12)
add(11, 12)
add(12, 12)

mul(10, 12)
mul(10, 12)

print(help(add))