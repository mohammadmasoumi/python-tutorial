# run twice 

def run_twice(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        res = f(*args, **kwargs)
        return res

    return wrapper

@run_twice
def add(a, b):
    print("add function has called with a: {a}, b: {b}")
    return a + b


add(10, 12)