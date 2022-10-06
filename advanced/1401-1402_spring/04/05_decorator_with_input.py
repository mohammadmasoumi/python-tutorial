def run_twice(n):

    def decorator(func):

        def wrapper(*args, **kwargs):
            # args: ("mohammad")
            # func: "ali"
            for _ in range(n):
                func(args[0] + "ali")
                func(args)
                func(*args)

        return wrapper

    return decorator


@run_twice(20)
# @decorator
def say_hello(name):
    print(f"Hello {name}, How are you?")

# wrapper("mohammad")
say_hello("mohammad")