
def summation(a, b):
    # a: 10, b: 12
    return a + b


def caller(f, x, y):
    # f: summation, x: 10, y: 12
    # summation(10, 12)
    result = f(x, y)
    # result: 22

    return result


print(     caller(summation, 10, 12)    )