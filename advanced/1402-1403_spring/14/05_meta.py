# frozendict

# class FrozenDict(dict):

#     def popitem(self):
#         raise ValueError("Can't change dict")


class Asghar:
    name = 'asghar'

    def introduce(self):
        print(f"Hello I am {self.name}")

    def my_khafan(self, a):
        print(f"I am khafan {a}")


a = Asghar()
# TypeError: 'mappingproxy' object does not support item deletion
# del Asghar.__dict__['my_khafan']
# Asghar.__dict__ = dict(Asghar.__dict__)
delattr(Asghar, 'my_khafan')
print(Asghar.__dict__)
print(a.__dict__)

a.my_khafan()
