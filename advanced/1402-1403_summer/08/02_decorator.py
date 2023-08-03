# decorator

def decorator(f):
    # 
    # state
    print("Hello")
    # 
    # Generalize
    def wrapper(*args, **kwargs):
        # if args[1] == 0:
        #     print("can't do that")
        #     return 
        res = f(*args, **kwargs)
        return res

    return wrapper


# wrapper = decorator(add)
@decorator
def add(a, b):
    return a + b

@decorator
def mul(a, b):
    return a * b


add(10, 12)
add(10, 12)


mul(10, 12)