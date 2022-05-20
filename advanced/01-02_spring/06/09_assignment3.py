def decorator(f):

    def wrapper(*args, **kwargs):
        args = tuple(map(lambda x: f"welcome {x}", args))
        kwargs = {k: f"welcome {v}" for k, v in kwargs.items()}
        
        # args: (1, 2, 3)
        # f(args) == f((1, 2, 3))
        # f(*args) == f(1, 2, 3)
        return f(*args, **kwargs)

    return wrapper


@decorator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  n                                                                                                                                                                                                                                         
def greeting(name):
    return name


print(greeting("asghar")) # args
print(greeting(name="asghar")) # kwargs
