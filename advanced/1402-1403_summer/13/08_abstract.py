
class MyAbstract:

    def create(self):
        raise NotImplementedError('you must override this function in the child class.')


class A(MyAbstract):

    def create(self):
        print('Hello ........')


a = A()
a.create()