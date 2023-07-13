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


# L(E) = E + merge(L(B) + L(D) + B + D)
# L(E) = E + merge(BO + DCBAO + B + D)
# L(E) = E + B + merge(O + DCBAO + D)
# L(E) = E + B + D + merge(O + CBAO)
# L(E) = E + B + D + C + merge(O + BAO)
# L(E) = E + B + D + C + B + merge(O + AO)
# L(E) = E + B + D + C + B + A + merge(O + O)
# L(E) = E + B + D + C + B + A + O
# L(E) = EBDCBAO

# L(D) = D + merge(L(C) + L(B) + C + B)
# L(D) = D + merge(CBAO + BO + C + B)
# L(D) = D + C + merge(BAO + BO + B)
# L(D) = D + C + B + merge(AO + O)
# L(D) = D + C + B + A + merge(O + O)
# L(D) = D + C + B + A + O
# L(D) = DCBAO

# L(C) = C + merge(L(B) + L(A) + B + A)
# L(C) = C + merge(BO + AO + B + A)
# L(C) = C + B + merge(O + AO + A)
# L(C) = C + B + A + merge(O + O)
# L(C) = C + B + A + O
# L(C) = CBAO

# L(B) = B + merge(L(O) + O)
# L(B) = BO

# L(A) = AO
