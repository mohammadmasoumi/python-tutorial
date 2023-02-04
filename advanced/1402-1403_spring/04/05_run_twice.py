def do_twice(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        return f(*args, **kwargs)

    return wrapper


@do_twice
def f():
    print("Hello")

f()