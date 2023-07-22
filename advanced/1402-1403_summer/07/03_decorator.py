def decorator_name(n):
    def decorator(f):
        # f: decorated function
        def wrapper(*args, **kwargs):

            if callable(n):
                res = f(*args, **kwargs)
            else:
                for _ in range(n):
                    # before executing function
                    res = f(*args, **kwargs)
                    # after executing function

            # res decorated function
            return res

        return wrapper

    if callable(n):
        # n: f
        # wrapper
        return decorator(n)

    return decorator

# n: func
# wrapper = decorator_name(add) [once] 
@decorator_name
def add(a, b):
    return a + b

# n: 10
# decorator = decorator_name(10)
# wrapper = decorator(add) 
@decorator_name(10)
# @decorator
def add(a, b):
    return a + b
