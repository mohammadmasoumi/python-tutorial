
class_name = input()


def khafan_function(self, a):
    print(f"I am khafan {a}")


a_properties = {
    'name': 'Asghar',  # input()
    'introduce': lambda self: print(f"Hello I am {self.name}"),
    'my_khafan': khafan_function
}

# self, __name: str, __bases: tuple[type, ...], __dict: dict[str, Any], **kwds: Any
# name, bases, properties
A = type(class_name, (), a_properties)

a = A()
a.introduce()
print(a.name)
print(type(a))
a.my_khafan(2)


class Asghar:
    name = 'asghar'

    def introduce(self):
        print(f"Hello I am {self.name}")

    def my_khafan(self, a):
        print(f"I am khafan {a}")


print("------------------------------------")
print(Asghar.__dict__)
print({key: value for key, value in Asghar.__dict__.items()
      if not key.startswith('__')})


class Akbar:
    pass


print("------------------------------------")
print(Akbar.__dict__)
print({key: value for key, value in Akbar.__dict__.items()
      if not key.startswith('__')})
