# implicitly inject some stuff to classes

class SerializerMetaclass(type):

    def __new__(cls, name, bases, props):
        instance = super().__new__(cls, name, bases, props)
        instance.errors = []

        return instance

# Serializer(db-instance) -> dict
# Serializer(data=dict) -> db-instance
class SerializerA(metaclass=SerializerMetaclass):
    # errors = []

    def __init__(self, name) :
        self.name = name

class SerializerB(metaclass=SerializerMetaclass):
    # errors = []

    def __init__(self, name) :
        self.name = name

