import functools


def smart_divide(f):

    @functools.wraps(f)
    def wrapper(a, b):
        if b == 0:
            print("Can't divide by zero!")
        else:
            return f(a, b)

    return wrapper

@smart_divide
def divide(a, b):
    print(a/b)

# Samples
divide(2, 5)
divide(2, 0)