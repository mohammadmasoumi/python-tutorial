
# _-call__


# def __call__(cls, *args, **kwargs):
#     self = cls.__new__(cls, *args, **kwargs)
#     cls.__init__(self, *args, **kwargs)


class A:

    def __call__(self, *args, **kwargs):

        print("Called me!")





# instance
a = A()  # __init__

# instace()
a()
