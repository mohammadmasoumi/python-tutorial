def add(a: int, b: int, c: int):
    return a + b + c


# a: arbotary (positional , keyword)
# b, c: keyword
def forced_add(a: int, *, b: int, c: int):
    return a + b + c


# sorted
print(add(10, 11, 12))
print(add(a=10, c=11, b=12))
print(add(10, c=11, b=12))
# print(add(10, 11, b=12)) # TypeError: add() got multiple values for argument 'b'
# print(a=10, b=11, 12) WRONG: positional + keyword

# TypeError: forced_add() takes 1 positional argument but 3 were given
# print(forced_add(10, 11, 12))
print(forced_add(a=10, c=11, b=12))
print(forced_add(b=10, c=11, a=12))
print(forced_add(10, c=11, b=12))
