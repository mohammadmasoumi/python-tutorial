class A:
    pass

class B:
    pass

class C(B, A):
    pass 

# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases B, C
class D(B, C):
    pass

print(D.__mro__)

"""
L(D) = D + merge(L(B), L(C), B, C)
     = D + merge(BO, CBAO, B, C)
     = D + B + merge(O, CBAO, C)
     = D + B + C + merge(O, BAO)
     = D + B + C + B + merge(O, AO)
     = D + B + C + B + A + merge(O, O)
     = D + B + C + B + A + O
     = DBCBAO

L(C) = C + merge(L(B), L(A), B, A)
     = C + merge(BO, AO, B, A)
     = C + B + merge(O, AO, A)
     = C + B + A + merge(O, O)
     = CBAO

"""