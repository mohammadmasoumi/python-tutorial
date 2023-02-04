
def decorator1(f):

    def wrapper(*args, **kwargs):
        print("%" * 40)
        res = f(*args, **kwargs)
        print("%" * 40)
        return res
    
    return wrapper

def decorator2(f):

    def wrapper(*args, **kwargs):
        print("*" * 40)
        res = f(*args, **kwargs)
        print("*" * 40)
        return res
    
    return wrapper

@decorator1
@decorator2
def function():
    print("Hello".center(40))


function()