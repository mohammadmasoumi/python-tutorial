
def star(f):
    def wrapper(*args, **kwargs):
        print("********")
        res = f(*args, **kwargs)
        print("********")
        return res

    return wrapper


def hashtag(f):
    def wrapper(*args, **kwargs):
        print("#########")
        res = f(*args, **kwargs)
        print("#########")
        return res

    return wrapper


@hashtag
@star
def fn():
    print("  Hello  ")


fn()
