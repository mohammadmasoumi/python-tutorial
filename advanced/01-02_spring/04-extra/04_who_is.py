

def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return wrapper


@decorator
def say_greeing():
    return "Hello, How are you"


# wrapper(*args, **kwargs) what?
print(help(say_greeing))
print("-----------------------------------------------")


# ------------------------------------------------------------
# How to solve this issue?
import functools

def decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return wrapper


@decorator2
def say_greeing2():
    return "Hello, How are you"


print(help(say_greeing2))

# press q to quit the help