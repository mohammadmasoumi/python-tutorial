# decorator without input
def logger(f):
    # function: f1
    def wrapper(*args, **kwargs):
        # args = (12, 13)
        print(f"args: {args}, kwargs: {kwargs}")
        # f(*args)
        # f(*(12, 13)) => f(12, 13)
        # f(**{"a": 12, "b": 13}) => f(a=12, b=13)
        # print()
        res = f(*args, **kwargs)
        # print()
        
        return res
        # return f(*args, **kwargs)

    return wrapper

@logger
def f1(a, b):
    return a * b

@logger
def f2(a):
    return a

print(f1(12, 13))
print(f2(12))

# print(f1(12, 13))
# w = logger(f1)
# print(w(12, 13))
