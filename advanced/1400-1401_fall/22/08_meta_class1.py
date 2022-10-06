# type(name, (), {})
# MetaClass
class MetaClass(type):
    #   type(name, (), {})
    def __new__(cls, name, bases, dct):
        print("Creating Instance in MetaClass")
        instance = super(MetaClass, cls).__new__(cls, name, bases, dct)
        instance.name = name

        return instance


class_name = input()

cls = MetaClass(class_name, (), {})
print(cls().name)
