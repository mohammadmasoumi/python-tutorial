# from abc import ABC, abstractmethod


def abstractmethod(f):

    def wrapper(*args, **kwargs):
        # try:
        #     res = f(*args, **kwargs)
        # except 
        raise NotImplementedError('you must override this function in the child class.')
    return wrapper


class MyAbstract:

    @abstractmethod
    def create(self):
        pass

class A(MyAbstract):
    pass
    # def create(self):
    #     print('Hello ........')


a = A()
a.create()