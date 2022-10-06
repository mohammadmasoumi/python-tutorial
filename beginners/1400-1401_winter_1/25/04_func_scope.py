a = 12

def add(a, b):
    # a = a[scope]
    print(f"[Inner] a: {a}, id(a): {id(a)}")
    a += 1
    print(f"[Inner] a: {a}, id(a): {id(a)}")
    return a + b

print(f"[Outer] a: {a}, id(a): {id(a)}")
print(add(a, 12))
print(f"[Outer] a: {a}, id(a): {id(a)}")
