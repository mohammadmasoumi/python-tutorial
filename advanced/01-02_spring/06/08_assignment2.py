
def italic(f):
    """
    F
    def func():
        # print("This is a basic program")
        return "This is a basic program"
    """

    def wrapper(*args, **kwargs):
        return f"<i>{f(*args, **kwargs)}</i>"

    return wrapper

def strong(f):

    """
    F
    @italic
    def func():
        # print("This is a basic program")
        return "This is a basic program"

    """
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        # RES: f"<i>{f(*args, **kwargs)}</i>"
        return f"<strong>{res}</strong>"

    return wrapper


@strong
@italic
def func():
    # print("This is a basic program")
    return "This is a basic program"


print(func())