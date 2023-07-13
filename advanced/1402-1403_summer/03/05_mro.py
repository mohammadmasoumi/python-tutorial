class A:
    pass


class B:
    pass


class C(B, A):
    pass


class D(B, C):
    pass


# MRO X
# D -> B -> C -> B -> A -> O
print(D.mro())

# left to right and merge

# l(D) = D + merge(L(B) + L(C) + B + C)
# L(D) = D + merge(BO + CBAO + B + C)
# L(D) = D + B + merge(O + CBAO + C)
# L(D) = D + B + C + merge(O + BAO)
# L(D) = D + B + C + B + merge(O + AO)
# L(D) = D + B + C + B + A + O
# L(D) = DBCBAO

# L(C) = C + merge(L(B) + L(A) + B + A)
# L(C) = C + merge(BO + AO + B + A)
# L(C) = C + B + merge(O + AO + A)
# L(C) = C + B + A + merge(O + O)
# L(C) = C + B + A + O
# L(C) = CBAO

# L(B) = B + merge(L(O) + O)
# L(B) = B + merge(O + O)
# L(B) = B + O
# l(B) = BO


# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases B, C
