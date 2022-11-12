def decorator1(f):
    """
    f
    @decorator2
    def chineese_greeting():
        print("Hello")
    """
    def wrapper(*args, **kwargs):
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        res = f(*args, **kwargs)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        return res

    return wrapper


def decorator2(f):
    """
    f
    chineese_greeting
    """
    def wrapper(*args, **kwargs):
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        res = f(*args, **kwargs)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        return res

    return wrapper


# @decorator1(f)

# f
# @decorator2
# def chineese_greeting():
#     print("Hello")

@decorator1
@decorator2
def chineese_greeting():
    print("Hello")


chineese_greeting()


"""
&&&&&&&&&&&&&&&&&&&&&&&&&&&&
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
&&&&&&&&&&&&&&&&&&&&&&&&&&&&
"""
