import functools

WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                       '__annotations__')


def decorator_name(f):
    # f: decorated function
    print("decorated function")

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # before executing function
        res = f(*args, **kwargs)
        # after executing function

        for func in WRAPPER_ASSIGNMENTS:
            setattr(wrapper, func, getattr(f, func))

        # res decorated function
        return res

    return wrapper


@decorator_name
def add(a, b):
    return a + b


# def fn():
#     pass


# print(help(fn))
# print("-------------")
print(help(add))

add(10, 12)
