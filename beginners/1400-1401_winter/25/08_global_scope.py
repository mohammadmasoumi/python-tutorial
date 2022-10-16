a = 12

def add(b, c):
    # b = a[scope]
    global a
    print(f"[Inner] a: {a}, id(a): {id(a)}")
    a += 1
    print(f"[Inner] a: {a}, id(a): {id(a)}")
    return b + c

print(f"[Outer] a: {a}, id(a): {id(a)}")
print(add(a, 12))
print(f"[Outer] a: {a}, id(a): {id(a)}")
