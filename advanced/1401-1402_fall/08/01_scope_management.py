"""
scope management:
    - global
    - nonlocal
    - local

search variable name:
    - local
    - nonlocal
    - global
"""
a = 12

def f1():
    # global a
    # a = a + 1
    a = 100

    def f2():
        nonlocal a
        a += 1
        print(a)
    
    print(a)
    f2()
    print(a)

print(a)
f1()
print(a)

