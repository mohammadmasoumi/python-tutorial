"""
f -> decorator -> f'

"""


def decorate(f):
    # f: test1
    def wrapper():
        print(f"Calling {f.__name__}, args: {()}, kwargs: {{}}")
        res = f()
        print(f"{f.__name__} called!")

        return res

    return wrapper

# wrapper = decorate(test1)
# test1()
# wrapper() 
@decorate
def test1():
    print("Test1")


@decorate
def test2():
    print("Test2")


test1()
test2()
