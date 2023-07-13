class A:
    pass


class B:
    pass


class C(A, B):
    pass


class D(C, A):
    pass


# L(C) = C + merge(L(P1)+L(P2)+...+P1+P2)

# L(D) = D + merge(L(C) + L(A) + C + A)
# L(D) = D + merge(CABO + AO + C + A)
# L(D) = D + C + merge(ABO + AO + A)
# L(D) = D + C + A + merge(BO + O)
# L(D) = D + C + A + B + O
# L(D) = DCABO

# L(C) = C + merge(L(A) + L(B) + A + B)
# L(C) = C + merge(AO + BO + A + B)
# L(C) = C + A + merge(O + BO + B)
# L(C) = C + A + B + merge(O + O)
# L(C) = C + A + B + O
# L(C) = CABO

# L(A) = A + merge(L(O) + O)  | L(O) = O
# L(A) = A + merge(O + O)
# L(A) = A + O
# L(A) = AO # mro: A -> O

# L(B) = BO


print(D.mro())
# D -> C -> A -> B -> O
