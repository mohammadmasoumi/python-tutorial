def f():
    print()
    print()
    print()
    print()
    print()


A = type('A', (), {'age': 100})
B = type("B", (A,), {'sayhi': lambda x: print("Hello")})
C = type("C", (B, A), {'khafan_function': f})
D = type("D", (B,), {'khafan_function': f})

# https://stackoverflow.com/questions/29214888/typeerror-cannot-create-a-consistent-method-resolution-order-mro
# E = type("D", (A, B), {'khafan_function': f})

# method resolution order
print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
print(D.__mro__)
print(E.__mro__)
# C = type("C", (A, B), {'khafan_function': f})


# class A:
#     age = 100

# class B(A):
#     def sayhi(self):
#         print("Hello")

a = A()

print(a)
print(A.__dict__)
print(a.__dict__)

b = B()
print(b)
print(B.__dict__)

c = C()
print(c)
print(C.__class__)

# def hello():
#     print("Hello")
#
#
# greeting = hello
#
# greeting()
