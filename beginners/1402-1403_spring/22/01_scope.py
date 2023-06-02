# global
a = 10

"""
- check local
- check nonlocal
- check global
"""

"""
nonlocal f3: f2->f1
nonlocal f2: f1
nonlocal f1: None

"""


def f1():
    a = 100

    def f2():
        # a = 1000
        # global a # a: 10
        # a = 12
        # a = a + 1
        # UnboundLocalError: local variable 'a' referenced before assignment
        # nonlocal a
        # a += 1

        def f3():
            nonlocal a
            a += 1
            b = a
            
            print(f"[f3:local] a: {a}, id(a): {id(a)}")  # 4

        print(f"[f2:local] a: {a}, id(a): {id(a)}")  # 3
        f3()
        print(f"[f2:local] a: {a}, id(a): {id(a)}")  # 5

    print(f"[f1:local] a: {a}, id(a): {id(a)}")  # 2
    f2()
    print(f"[f1:local] a: {a}, id(a): {id(a)}")  # 6


print(f"[global] a: {a}, id(a): {id(a)}")  # 1
f1()
print(f"[global] a: {a}, id(a): {id(a)}")  # 7
