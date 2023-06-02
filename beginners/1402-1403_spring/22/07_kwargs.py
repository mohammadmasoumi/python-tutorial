# kwargs

def add(**kwargs):
    # **kwargs = a=10, b=20, c=30 pack
    # kwargs: {'a': 10, 'b':20, 'c':30}
    # **kwargs=> 'a': 10, 'b':20, 'c':30 unpack
    # {**kwargs}
    print(kwargs, type(kwargs))
    return sum(kwargs.values())


print(add(a=10, b=20, c=30))
print(add(c=10, b=20, a=30))
