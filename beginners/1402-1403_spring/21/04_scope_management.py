"""
scope management
    - global
    - local
    - nonlocal

FIND FOR VARIABLE
    - local scope
    - nonlocal scope
    - global scope
"""
# a: global
a = 12

def f1():
    a = 13 # a: local
    print(f"[f1] a: {a}, id(a):{id(a)}")


print(f"[main] a: {a}, id(a):{id(a)}")
f1()
print(f"[main] a: {a}, id(a):{id(a)}")
