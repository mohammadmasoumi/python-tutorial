# args, kwargs

# args: positional argument
# kwargs: keyword arguments

"""
inputs: 0 or OO
outputs: 1 or OO
"""

# a, b, *c = 1, 2, 3, 4

# naming convention: args
"""
def add(*asghar):
    return sum(asghar)
"""


def add(*args):
    # *args = 1, 2, 3 packing
    # args: (1, 2, 3)
    # *args: 1, 2, 3 unpacking
    # print(type(args)) : tuple
    return sum(args)


print(add(1, 2, 3))
print(add(1, 2, 3, 4))
print(add(1, 2, 3, 4, 5))


def add2(my_list):
    # other language
    # pass dynamic length values
    pass


def add(a, b, *args):
    # *args = 1, 2, 3 pack (assignment)
    # args: (1, 2, 3)
    # [*args] unpack
    # [1, 2, 3]
    # a: 1, b:2, args: (3, 4, 5)
    # [a, b, *args]   *args => 3, 4, 5
    # [1, 2, 3, 4, 5]
    # [a, b, args]   args => (3, 4, 5)
    # [1, 2, (3, 4, 5)]
    return sum([a, b, *args])


print(add(1, 2, 3))  # a: 1, b: 2, args:(3, )
print(add(1, 2, 3, 4))  # a:1, b:2, args: (3, 4)
print(add(1, 2, 3, 4, 5))  # a:1, b:2, args: (3, 4, 5)


# TypeError: add() missing 2 required keyword-only arguments: 'a' and 'b'
def add(*args, a, b):
    return sum([a, b, *args])


# print(add(1, 2, 3))
print(add(1, 2, a=3, b=4))
# print(add(1, 2, 3, 4, 5))
