# a: global
a = 12
b = 13
"""
a -/> 12
a -> 13
"""

def f1():
    global a, b # write, update value
    a += 1 # a(global) = a(global) + 1
    print(f"[f1] a: {a}, id(a):{id(a)}")


print(f"[main] a: {a}, id(a):{id(a)}")
f1()
print(f"[main] a: {a}, id(a):{id(a)}")
