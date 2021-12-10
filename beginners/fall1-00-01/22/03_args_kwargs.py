def func(*args, **kwargs):
    # args: (10, 12)
    # kwargs: {'a': 12, 'b': 12}
    print(args, kwargs)


func(10, 12, a=12, b=12)


# func(a=12, b=12, 10, 12) # kwargs must be the last items


# پارامترهایی که بعد از ستاره می آیند باید بصورت key value بیایند
def func1(*, a, b):
    print(a, b)


def func3(a, b, *, c):
    print(a, b, c)


# no args and kwargs after *
# def func4(a, b, *, *c):
#     print(a, b, c)
#
#
# def func5(a, b, *, **c):
#     print(a, b, c)


# func1(12, 13)
func1(a=12, b=13)
func3(a=5, b=6, c=7)
func3(5, 6, c=7)
func3(5, 6, c=7)


#        default value
def func2(a=12, b=13):  # a, b
    print(f"a: {a}, b: {b}")


#     a  b => default value
func2(12)  # 12 [a]?b, b: default value
#      a   b
func2(22, 23)  # 12 [a]?b
func2(b=22, a=23)  # 12 [a]?b
# func2(,12)  raise exception
# func2(None, 12) a: None, b: 12
#     a = default value, b = 12
func2(b=12)
