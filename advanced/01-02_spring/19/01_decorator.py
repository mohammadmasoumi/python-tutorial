
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before!")
        result = func(*args, **kwargs)
        print("After!")

        return result

    return wrapper


@decorator
def test(name):

    print(f"name: {name}")


test("Ali")


