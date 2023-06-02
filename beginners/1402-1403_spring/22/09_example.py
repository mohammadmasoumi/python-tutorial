
def test1(*args, **kwargs):
    print(f"args: {args}, kwargs: {kwargs}")


test1(10)  # args: (10), kwargs: {}
test1(a=10)  # args: (), kwargs: {'a': 10}
test1(10, a=10)  # args: (10), kwargs: {'a': 10}
