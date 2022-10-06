from enum import Enum

class DuplicateFreeEnum(Enum):
    def __init__(self, *args):
        cls = self.__class__
        # cls.__members__
        # for shape in Shape:
        if any(self.value == e.value for e in cls):
            a = self.name
            e = cls(self.value).name
            raise ValueError(
                "aliases not allowed in DuplicateFreeEnum:  %r --> %r"
                % (a, e))

class Color(DuplicateFreeEnum):
    RED = 1
    GREEN = 2
    BLUE = 3
    GRENE = 2