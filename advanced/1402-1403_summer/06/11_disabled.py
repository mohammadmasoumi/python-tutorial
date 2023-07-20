# disabled 

def disabled(f):
    def wrapper(*args, **kwargs):
        pass

    return wrapper

@disabled
def add(a, b):
    print("add function has called with a: {a}, b: {b}")
    return a + b


add(10, 12)