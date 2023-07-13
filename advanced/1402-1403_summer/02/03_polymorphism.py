
def add(a, b):
    return a + b

#           c, d


def multipy(a, b):
    return a * b


def divide(a, b):
    return a / b


# polymorphism
functions = [add, multipy, divide]

for func in functions:
    print(func(a=12, b=6))
