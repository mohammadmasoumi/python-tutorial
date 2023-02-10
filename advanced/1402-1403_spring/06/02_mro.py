# method resolution order

# A(Object)
class A:
    pass

class B:
    pass

class C(A, B):
    pass 

class D(C, B):
    pass

"""
L(class) = class + merge(L(C1), L(C2), ..., L(Cn), C1, C2, ..., Cn)

# 
merge(AO, O)
A + merge(O, O)
A + O
AO

L(D) = D + merge(L(C), L(B), C, B)
     = D + merge(CABO, BO, C, B)
     = D + C + merge(ABO, BO, B)
     = D + C + A + merge(BO, BO, B)
     = D + C + A + B + merge(O, O)
     = D + C + A + B + O
     = DCABO

L(C) = C + merge(L(A), L(B), A, B)
     = C + merge(AO, BO, A, B)
     = C + A + merge(O, BO, B)
     = C + A + B + merge(O, O)
     = C + A + B + O
     = CABO

L(A) = A + merge(L(O), O)
     = A + merge(O, O)
     = A + O
     = AO 
L(B) = BO

"""
