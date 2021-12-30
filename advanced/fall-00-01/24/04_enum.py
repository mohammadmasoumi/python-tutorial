from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2
    PINK = 3

    @classmethod
    def items(cls):
        for item in cls.__members__:
            # cls == Color
            main_item = cls[item]  # item => name
            # main_item: Color.RED  |  Color['RED']
            yield main_item.name, main_item.value
            # yield main_item.name, main_item.value
            # yield cls[item].name, cls[item].value

            # cls.item  != cls.RED


# color: Color.RED, Color.BLUE
for color in Color:
    print(color, color.name, color.value)

for name, value in Color.items():
    print(f"name: {name}, value: {value}")

gen = Color.items()
print(type(gen))
for name, value in gen:
    print(f"name1: {name}, value: {value}")

for name, value in gen:
    print(f"name2: {name}, value: {value}")









