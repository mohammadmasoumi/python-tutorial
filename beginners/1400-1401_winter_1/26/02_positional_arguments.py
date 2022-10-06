
# positional arguments
def add(a, b):
    print(f"a: {a}, b: {b}")
    return a + b

def minus(a, b):
    print(f"a: {a}, b: {b}")
    return a - b


# call, invoke
print(add(12, 13)) # a = 12, b = 13
print(add(13, 12)) # a = 13, b = 12

print(minus(12, 13)) # a = 12, b = 13
print(minus(13, 12)) # a = 13, b = 12

# keyword arguments
print(add(b=12, a=13)) # a = 13, b = 12
print(add(a=13, b=12)) # a = 13, b = 12

# .sort(key=func)
# [].sort()

# combination
def add(a, b, c, d):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
    return a + b + c + d

print(add(12, 13, d=14, c=10))
# SyntaxError: positional argument follows keyword argument
# print(add(a=12, b=13, 14, 10))

# TypeError: add() got multiple values for argument 'a'
# print(add(12, 13, a=14, b=10))

# force
def add(a, *, b, c, d):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
    return a + b + c + d

# TypeError: add() takes 1 positional argument but 2 positional arguments (and 2 keyword-only arguments) were given
# print(add(12, 13, d=14, c=10))

print(add(12, d=13, b=14, c=10))

def add(a, b, *, c, d):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
    return a + b + c + d

print(add(12, 13, d=14, c=10))