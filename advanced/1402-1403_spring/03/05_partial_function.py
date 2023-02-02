# who is?

def handler(*args, **kwargs):
    """This is handler"""
    print(f"Handled, args: {args}, kwargs: {kwargs}")

def partial_function(f, *args, **kwargs):
    def partial(*fargs, **fkwargs):
        return f(*args, *fargs, **{**kwargs, **fkwargs})

    print(partial)

    partial.__dict__ = f.__dict__
    partial.__qualname__ = f.__qualname__
    partial.__name__ = f.__name__
    partial.__doc__ = f.__doc__
    
    print(partial)
    
    return partial

my_partial = partial_function(handler, "asghar", 22)
# <function partial_function.<locals>.partial at 0x000001AD167BF0A0>
# print(my_partial)
# print(handler)
