def adder(*, a, b):
    print(f"a: {a}")
    print(f"b: {b}")

    return a + b

def adder2(a, *, b, c):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"b: {c}")

    return a + b + c

