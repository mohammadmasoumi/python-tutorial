# a: global
a = 12
b = 13
"""
a -/> 12
a -> 13
"""

def f1():
    print(f"[f1] a: {a}, id(a):{id(a)}")


print(f"[main] a: {a}, id(a):{id(a)}")
f1()
print(f"[main] a: {a}, id(a):{id(a)}")
