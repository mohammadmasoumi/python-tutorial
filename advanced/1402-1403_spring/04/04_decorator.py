
def decorator(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper

@decorator
def hassan():
    pass

# f: wrapper
# f = decorator(hassan)
# f("asghar")
hassan()

def f(*a, **b):
    # a: (12, 13, 14, 15), b: {}
    # a: (), b: {"a": 12, "b": 13, "c": 14, "d": 15}
    # a: (12, 13), b: {"a": 14, "b": 15}
    print(a, b)

f(12, 13, 14, 15) # positional argument
f(a=12, b=13, c=14, d=15) # keywords argument
f(12, 13, a=14, b=15)