
def run(num):

    def decorator(f):

        def wrapper():
            for _ in range(num):
                f()

        return wrapper

    return decorator


@run(2)
def hello(name):
    print(f"Hello Teacher {name}")


hello("Mohammad")
