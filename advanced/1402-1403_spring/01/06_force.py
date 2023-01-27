def add3(a,* ,b, c):
    return a + b + c

def fcuntion1(a, *, options, b=13, c=14):
    return a + b + c

def fcuntion2(a, b=13, c=14, *, options):
    return a + b + c

# TypeError: add3() takes 1 positional argument but 3 were given
# positional argument
# print(add3(12, 13, 14))
print(add3(12, b=13, c=14))


fcuntion1(12, options={})