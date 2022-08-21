from enum import Enum


class Coordinate(bytes, Enum):
    """
    Coordinate with binary codes that can be indexed by the int code.
    """
    def __new__(cls, value, label, unit):
        obj = bytes.__new__(cls, [value])
        # name
        # _value_
        # object.value
        obj._value_ = value
        obj.label = label
        obj.unit = unit

        return obj

    PX = (0, 'P.X', 'km')
    PY = (1, 'P.Y', 'km')
    VX = (2, 'V.X', 'km/s')
    VY = (3, 'V.Y', 'km/s')


print(list(Coordinate))
print(Coordinate.PX.label)
print(Coordinate.PX.unit)

# class A:

#     pass

# A = type('a', (), {})
# a = A()
# print(a())