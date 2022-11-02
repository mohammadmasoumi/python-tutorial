# forced C called with key word argument
def add(a, b, *, c):
    return a + b + c

# TypeError: add() takes 2 positional arguments but 3 were given
# print(add(10, 12, 13))
print(add(10, 12, c=13))
print(add(a=10, b=12, c=13))