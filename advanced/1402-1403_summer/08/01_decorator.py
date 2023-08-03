# decorator

def decorator(f):
    # Generalize
    def wrapper(*args, **kwargs):
        pass

    return wrapper

# def decorator(f):
    def wrapper(a1, b1):
        pass

    return wrapper


# decorator()
@decorator
def add(a, b):
    return a + b


@decorator
def add3(a, b, c):
    return a + b + c

add(10, 12)
add(a=10, b=12)