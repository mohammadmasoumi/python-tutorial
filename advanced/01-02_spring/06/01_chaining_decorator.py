
def decorator1(f):

    def wrapper(*args, **kwargs):
        print("*************")
        res = f(*args, **kwargs)
        print("*************")
        return res

    return wrapper


def decorator2(f):

    def wrapper(*args, **kwargs):
        print("%%%%%%%%%%%%%%%")
        res = f(*args, **kwargs)
        print("%%%%%%%%%%%%%%%")
        return res

    return wrapper

def decorator3(f):

    def wrapper(*args, **kwargs):
        print("&&&&&&&&&&&&&&&&&&&")
        res = f(*args, **kwargs)
        print("&&&&&&&&&&&&&&&&&&&")
        return res

    return wrapper

@decorator1
@decorator2
@decorator3
def say_greeting():
    print("Hello, How are you?")


say_greeting()