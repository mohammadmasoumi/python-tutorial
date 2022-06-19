

class A1:

    # def method1(self):
    #     print(f"[{self.__class__.__name__} | A1] Hello")
    pass


class A2:

    # def method1(self):
    #     print(f"[{self.__class__.__name__} | A2] Hello")
    pass

class B1(A1, A2):

    # def method1(self):
    #     print(f"[{self.__class__.__name__} | B1] Hello")
    pass

class B2:

    # def method1(self):
    #     print(f"[{self.__class__.__name__} | B2] Hello")
    pass

class C1(B1, B2):

    # def method1(self):
    #     print(f"[{self.__class__.__name__} | C1] Hello")
    pass

class C2:

    # def method1(self):
    #     print(f"[{self.__class__.__name__} | C2] Hello")
    pass

class D1(C1, C2):

    # def method1(self):
    #     print(f"[{self.__class__.__name__} | D1] Hello")
    pass

class D2:

    # def method1(self):
    #     print(f"[{self.__class__.__name__} | D2] Hello")
    pass

class E(D1, D2):

    # def method1(self):
    #     print(f"[{self.__class__.__name__} | E] Hello")
    pass


e = E()
e.method1()
# AttributeError: 'E' object has no attribute 'method1'