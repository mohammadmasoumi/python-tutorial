def logger_decorator(f):
    # f: greeting
    def wrapper():
        print(f"Start {f.__name__}")
        res = f()
        print(f"End {f.__name__}")
        
        return res

    return wrapper


@logger_decorator
def greeting():
    print("Hello, How are you?")
    return "asghar"


# wrapper = logger_decorator(greeting)
# name = wrapper()
name = greeting()
print(name)
