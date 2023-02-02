
def partial_function(f, *args, **kwrags):

    def wrapped_function(*fargs, **fkwargs):

        return f(*args, *fargs, **{**kwrags, **fkwargs})

    wrapped_function.func = f
    wrapped_function.args = args
    wrapped_function.keywords = kwrags

    return wrapped_function


def f(a, b):
    return a + b


print(dir(f))
print(dir(partial_function(f, 10, 20)))