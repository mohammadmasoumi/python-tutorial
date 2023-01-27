def add(a, b):
    print(f"a: {a}, b: {b}")
    return a + b

def mul(a, b):
    print(f"a: {a}, b: {b}")
    return a * b

def div(a, b):
    print(f"a: {a}, b: {b}")
    return a * b

def caller(f, a, b):
    print(f"a: {a}, b: {b}")
    res =  f(a, b)
    print(f"a: {a}, b: {b}")
    return res

a = add(12, 13)
b = mul(12, 13)
a = caller(add, 12, 13)
b = caller(mul, 12, 13)