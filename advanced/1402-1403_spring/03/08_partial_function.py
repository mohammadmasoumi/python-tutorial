# who is?
import functools

def handler(*args, **kwargs):
    """This is handler"""
    print(f"Handled, args: {args}, kwargs: {kwargs}")

def partial_function(f, *args, **kwargs):
    
    @functools.wraps(f)
    def partial(*fargs, **fkwargs):
        return f(*args, *fargs, **{**kwargs, **fkwargs})

    return partial

my_partial = partial_function(handler, "asghar", 22)
# <function partial_function.<locals>.partial at 0x000001AD167BF0A0>
print(my_partial)
