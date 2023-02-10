class A:
    pass


class B:
    pass


class C(B, A):
    pass


class D(C, B):
    pass


class E(B, D):
    pass


"""
L(E) = E + merge(L(B), L(D), B, D)
     = E + merge(BO, DCBAO, B, D)
     = E + B + merge(O, DCBAO, D)
     = E + B + D + merge(O, CBAO)
     = E + B + D + C + merge(O, BAO)
     = EBDCBAO

"""