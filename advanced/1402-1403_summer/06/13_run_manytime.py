# decorator with input
              
def run_twice(n): # bind n to decorator
    def decorator(f):
        def wrapper(*args, **kwargs):
            res = None
            for _ in range(n):
                res = f(*args, **kwargs)
            return res
        return wrapper
    return decorator

# wrapper = run_twice(f)
# wrapper(a, b)

# @run_twice function

# decorator = run_twice(10)
# wrapper = decorator(add)
# wrapper()
@run_twice(5)
def add(a, b):
    print("add function has called with a: {a}, b: {b}")
    return a + b


add(10, 12)