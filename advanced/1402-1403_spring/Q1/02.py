import functools

CALLED_FUNCTIONS = []
CALLED_FUNCTIONS2 = set()

def register(f):

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func_name = f.__name__

        if func_name not in CALLED_FUNCTIONS:
            CALLED_FUNCTIONS.append(func_name)

        CALLED_FUNCTIONS2.add(func_name)

        res = f(*args, **kwargs)
        return res

    return wrapper

@register
def f1():
    pass

@register
def f2():
    pass

for _ in range(3):
    f1()
    f2()


print(CALLED_FUNCTIONS)
print(CALLED_FUNCTIONS2)