from enum import Enum

# repr()
# str()

class NoValue(Enum):
    def __repr__(self):
        return f'<{self.__class__.__name__}.{self.name}>'


class AutoNumber(NoValue):
    def __new__(cls):
        print(cls.__name__)
        print(dir(cls))
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

class Color(AutoNumber):
    RED = ()
    GREEN = ()
    BLUE = ()

print(Color.RED.value)