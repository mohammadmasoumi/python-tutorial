
"""
class MyFavoriteClass:

    def dummy_function(self):
        print("Thank you ostad!")

"""
class MyFavoriteClass:
    
    def dummy_function(self):
        print("Thank you ostad!")

class Metaclass(type):

    def __new__(cls, name, bases, d):
        # instance: class
        # bases += (MyFavoriteClass, )
        bases = (MyFavoriteClass, )
        instance = super().__new__(cls, name, bases, d)
        return instance

class D:
    pass

class A(D, metaclass=Metaclass):
    pass

class B(D, metaclass=Metaclass):
    pass

class C(D, metaclass=Metaclass):
    pass


a = A()
a.dummy_function()