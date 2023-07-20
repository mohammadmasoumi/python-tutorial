# decorator
# caller(f, *args, **kwargs)

def decorator(f):
    # f, *args, **kwargs
    def wrapper(*args, **kwargs):
        # args: (10, 12)
        # args: (11, 13)
        # before calling f
        res = f(*args, **kwargs)
        # after calling f
        return res

    return wrapper

"""
wrapper
|-------|
|   f   |
|-------|

f() -> wrapper()

wrapper() -> f()
"""

# wrapper = decorator(add)
@decorator
def add(a, b):
    return a + b

# wrapper(10, 12)
add(10, 12)

# wrapper(11, 13)
add(11, 13)


# def my_add():
#     pass

# # alias
# my_sum = my_add
# my_sum()
# my_add()
