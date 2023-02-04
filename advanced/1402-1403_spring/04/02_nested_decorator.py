
def d1(f):
    # f: d2.wrapper
    def wrapper(*args, **kwargs):
        print("*******")
        res = f(*args, **kwargs)
        print("*******")
        return res
    
    return wrapper

def d2(f):
    # f: f1
    def wrapper(*args, **kwargs):
        print("%%%%%%%")
        res = f(*args, **kwargs)
        print("%%%%%%%")
        return res
    
    return wrapper

@d1  # @d1
@d2  # wrapper
def f1(name):
    print(f"hello, {name}")

f1("ali")