# a: global
a = 12

def f1():
    # UnboundLocalError: local variable 'a' referenced before assignment
    # define variable a
    # a = a(local) + 1
    a += 1 # a = a + 1
    print(f"[f1] a: {a}, id(a):{id(a)}")


print(f"[main] a: {a}, id(a):{id(a)}")
f1()
print(f"[main] a: {a}, id(a):{id(a)}")
