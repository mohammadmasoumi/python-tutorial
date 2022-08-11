
class MetaClass(type):

    def __new__(cls, name,  bases, dct):
        instance = super(MetaClass, cls).__new__(cls, name, bases, dct)
        props = list(filter( lambda x: not x.startswith("__"), instance.__dict__))
        print(props)

        for item in props:
            # print(getattr(instance, item))
            value = getattr(instance, item)
            setattr(instance, item, instance(name=item.lower(), value=value))

        return instance


class MyEnum(metaclass=MetaClass):
    
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value


class Shape(MyEnum):
    RECTANGLE = "rect" # Shape(rectangle, "rect")
    TRIANGLE = "tri"
    CICLE = "circ"


print(Shape.RECTANGLE.name)
print(Shape.RECTANGLE.value)

