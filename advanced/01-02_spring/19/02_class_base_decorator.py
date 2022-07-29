
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before!")
#         result = func(*args, **kwargs)
#         print("After!")
#         return result
#     return wrapper


# @decorator
# def test(name):

#     print(f"name: {name}")

# test("Ali")
# decorator = Decorator("Asghar")
# # decorator.__call__() 
# decorator("Bye")


class Decorator1:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"args: {args}, kwargs: {kwargs}")
        result = self.func(*args, **kwargs)

        return result


@Decorator1
def test(name):
    print(name)

test("asghar")