class C1:
    pass

class C2:
    pass

class A1:
    pass

class A2(C1, C2):
    pass

class B1(A2, A1):
    pass

class E(A2, B1):
    pass

e = E()
e.method1()
# AttributeError: 'E' object has no attribute 'method1'