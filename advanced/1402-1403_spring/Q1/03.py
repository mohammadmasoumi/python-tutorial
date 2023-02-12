import functools


"""
See: 
https://docs.python.org/3/tutorial/inputoutput.html
https://www.geeksforgeeks.org/open-a-file-in-python/
"""
def register(f):

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        with open("logger.txt", "a") as file:
            file.write(f"function {f.__name__} called with args: {args}, kwargs: {kwargs}\n")

        return f(*args, **kwargs)

    return wrapper



@register
def f1(a, b):
    pass

@register
def f2(a, b, c):
    pass

for i in range(3):
    f1(i, b=f"name_{i}")
    f2(f"name_{i}", b=i+1, c=1+2)