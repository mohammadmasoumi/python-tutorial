#
# closure (sth) binding (fuction)

def logger_decorator(f):
    # f: greeting
    def wrapper():
        print(f"Running {f.__name__}")
        return f()

    return wrapper


@logger_decorator
def greeting():
    print("Hello, How are you?")


greeting()
