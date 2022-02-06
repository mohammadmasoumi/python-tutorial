# The reduce function reduces a collection using a binary operator to combine items two at a time

from functools import reduce


def my_add(x, y):
    return x + y


# another implementation of the sum function
print(reduce(my_add, [1, 2, 3, 4, 5]))
