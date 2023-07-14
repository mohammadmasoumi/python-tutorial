
def logger(f):
    def wrapper(*args, **kwargs):
        print(f"Calling {f.__name__} with args: {args}, kwargs: {kwargs}")
        res = f(*args, **kwargs)
        print(f"{f.__name__} has called!")

        return res
    return wrapper

# wrapper = logger(add)
# wrapper(10, 12)


@logger
def add(a, b):
    return a + b


@logger
def multi(a, b):
    return a * b


add(10, 12)
multi(10, 12)
