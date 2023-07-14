def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def dummy():
    print("Dummy")


def caller(f, *args, **kwargs):
    # f: add, args: (10, 12)
    # f: dummy
    print(f"Calling {f.__name__}, args: {args}, kwargs: {kwargs}")
    # res = add(10, 12), res: 22
    # res = dummy(), res: None
    # res = None
    res = f(*args, **kwargs)  # wrapp into 2 prints
    print(f"{f.__name__} called!")

    return res


# deligation
print(caller(add, a=10, b=12))  # keyword argument
print(caller(add, 10, 12))  # positional argument
print(caller(divide, 10, 12))
print(caller(dummy))
