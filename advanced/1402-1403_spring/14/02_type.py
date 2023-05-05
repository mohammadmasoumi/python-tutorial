
class A:
    def introduce(self):
        print("I am asghar")

a = A()

print(type(a)) # A
print(type(A)) # type
print(a.__class__) # A
print(type.__class__)

#   class A         class A
print(type(a) is a.__class__)

