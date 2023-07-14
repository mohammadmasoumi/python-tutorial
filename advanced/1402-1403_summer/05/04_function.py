
def f(a, b):  # a, b: params

    return a + b


# positional
# a: 10, b: 12
print(f(10, 12))

# keyword argument
# key: value
print(f(a=10, b=12))  # argument
print(f(b=10, a=12))


def advanced_f(*args, **kwargs):
    # packing
    # *args = 10, 12, args: (10, 12)
    # unpacking
    # args: (10, 12)
    # *args: 10, 12
    # [*args] => [10, 12]  X ~~[(10, 12)]~~
    print(f"args: {args}, kwargs: {kwargs}")
    pass


advanced_f(10, 12)

# packing
# a: 10, b: (12, 13, 14)
a, *b = 10, 12, 13, 14

# a: 10, b: 12
a, b = 10, 12
