# args, kwargs

def add(*args, **kwargs):
    # args: (1, 2, 3)
    # *args => 1, 2, 3
    # [*args] => [1, 2, 3]
    # kwargs: {'a': 10,'b': 20, 'c': 30}
    # kwargs.values() => [10, 20, 30]
    # *kwargs.values() => 10, 20, 30
    # [*kwargs.values()] => [10, 20, 30]
    # [*args, *kwargs.values()] => [1, 2, 3, 10, 20, 30]
    return sum([*args, *kwargs.values()])


# positional -> args
# keyword -> kwargs
# first -> positional arguments
# following -> keyword arguments
add(1, 2, 3, a=10, b=20, c=30)
# add(1, b=20, 3, a=10, 2, c=30) WRONG
