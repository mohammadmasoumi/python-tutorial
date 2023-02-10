class A:
    pass

class B:
    pass

class C(B, A):
    pass 

class D(C, B):
    pass

print(D.__mro__)

"""
L(D) = D + merge(L(C), L(B), C, B)
     = D + merge(CBAO, BO, C, B)
     = D + C + merge(BAO, BO, B)
     = D + C + B + merge(AO, O)
     = D + C + B + A + merge(O, O)
     = D + C + B + A + O
     = DCBAO

L(C) = C + merge(L(B), L(A), B, A)
     = C + merge(BO, AO, B, A)
     = C + B + merge(O, AO, A)
     = C + B + A + merge(O, O)
     = CBAO

"""