# mro 0 inheritance
# method resolution order
# from left parent to right parent
# __func__ dunder method or magic function

class A1:

    def method1(self):
        print("[method1]: Hello I am in A1")

    def method7(self):
        print("[method7]: Hello I am in A1")

class A3:
    
    def method11(self):
        print("[method11]: Hello I am in A3")

class A2:
    
    def method10(self):
        print("[method10]: Hello I am in A2")

    def method11(self):
        print("[method11]: Hello I am in A2")

class B1(A1, A3):

    def method1(self):
        print("[method1]: Hello I am in B1")

    def method5(self):
        print("[method5]: Hello I am in B1")

class B2(A2):

    def method2(self):
        print("[method2]: Hello I am in B2")

    def method6(self):
        print("[method6]: Hello I am in B2")

class C(B1, B2):

    def method1(self):
        print("[method1]: Hello I am in C")


c1 = C()
c1.method6()
# 1. is method6 in C
# 2. [most left parent]: B1 | is method6 in B1
# 3. is method6 in B1 parent[A1] | is method6 in A1
# 4. is method6 in B2 [next parent]

c1.method5()
# 1. is method5 in C
# 2. [most left parent]: B1 | is method5 in B1

c1.method10()
# 1. is method10 in C
# 2. [most left parent]: B1 | is method10 in B1
# 3. is method10 in B1 parent[A1] | is method6 in A1
# 4. is method10 in B2 [next parent]
# 5. is method10 in B2 parent[A2] | is method6 in A2

c1.method11()
