class E: pass

class D(object): pass

class C(object): pass

class B(D, E): pass

class A(B, C): pass


# (head)ABCD[tail]
# L[class] = class + merge(L[C1], L[C2], ... L[Cn], C1, C2, ..., Cn) 

# L[E] = E + merge(L[O], O)
# L[E] = E + merge(O, O)
# l[E] = E + O => EO

# L[D] = D + merge(L[O], O)
# L[D] = D + merge(O, O)
# L[D] = DO

# L[C] = CO

# B(D, E) = B + merge(L[D], L[E], D, E)
# B(D, E) = B + merge(DO, EO, D, E)
# B(D, E) = B + merge(DO, EO, D, E)
# B(D, E) = B + D + merge(O, EO, E)
# B(D, E) = B + D + E + merge(O, O)
# B(D, E) = B + D + E + O => BDEO

# L[class] = class + merge(L[C1], L[C2], ... L[Cn], C1, C2, ..., Cn) 
# L[A] = A + merge(L[B] + L[C] + B + C)
# L[A] = A + merge(BDEO + CO + B + C)
# L[A] = A + B + merge(DEO + CO+ C)
# L[A] = A + B + D + merge(EO + CO+ C)
# L[A] = A + B + D + E + merge(O + CO+ C)
# L[A] = A + B + D + E + C + merge(O + O)
# L[A] = A + B + D + E + C + O

print(A.__mro__)

# L[A] = A + merge(L[B], L[C], B, C)
#  
