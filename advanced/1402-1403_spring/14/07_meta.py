cls_name = input()


class Asghar:

    def __init__(self, name):
        self.name = name


A = type(cls_name, (), {})

asghar1 = Asghar(name='asghar')
asghar2 = A()

print(asghar1 is asghar2)


class A:

    def __init__(self):
        pass


class A:
    pass


print(A())
