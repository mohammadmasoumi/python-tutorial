
# a, b, *c = [1, 2, 3 ,4]
# a1 = 10, 20 # tuple
# print(a, b, c)

# positional argument
# def pos(a, b):
#     return a + b

# pos(10, 20)
# pos(20, 10)

def unlimited_args(*asghar):
    # *asghar = 10, 20
    # args
    print(asghar, type(asghar))


# positional args
unlimited_args(10, 20)
unlimited_args(10, 20 , 30)


def unlimited_kwargs(**asghar):
    # asghar = {'a': 10, 'b': 20}
    # args
    print(asghar, type(asghar))


# key-value args
unlimited_kwargs(a=10, b=20)
unlimited_kwargs(a=10, b=20, c=30)


def unlimited_args_kwargs(*asghar,**akbar):
    # asghar: (10, )
    # akbar: {'b': 20}
    print(asghar, type(asghar))
    print(akbar, type(akbar))


# positiona, key-value args
unlimited_args_kwargs(10, b=20)
unlimited_args_kwargs(10, b=20, c=30)
