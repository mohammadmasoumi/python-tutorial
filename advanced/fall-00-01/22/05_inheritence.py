"""
A         B
  \      /
     D         C
       \     /
         E
"""


class A:
    def test(self):
        print(f"[{self.__class__.__name__}, A]")


class B:
    pass


class C:
    def test(self):
        print(f"[{self.__class__.__name__}, C]")


class D(A, B):
    pass


class E(D, C):
    pass


e = E()
e.test()
