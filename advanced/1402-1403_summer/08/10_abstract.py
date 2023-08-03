
from abc import ABC, abstractmethod, abstractclassmethod

class AbstractClass(ABC):

    @abstractmethod
    def test_a(self):
        pass

    @abstractmethod
    def test_b(self, a, b, c):
        # bad smell, bad practice
        print("b in abstract method")
        d = a + b + c
        return d

    @abstractclassmethod
    def class_a(cls):
        pass

class A(AbstractClass):

    def test_a(self):
        print("Test A")

    def test_b(self, a, b):
        res = super().test_b(a, b, 10)
        print("Test A")
        return res + a + b

    @classmethod
    def class_a(cls):
        print(cls.__name__)
        
# TypeError: Can't instantiate abstract class A with abstract method test_b
a = A()
print(a.test_b(10, 12))
    