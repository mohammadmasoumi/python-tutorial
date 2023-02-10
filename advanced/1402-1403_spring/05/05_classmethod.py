"""
                - property
- instance level 
                - behaviour

                - property
- class level
                - behaviour

"""


class Bomb:
    # classproperty
    BOMBS = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

        Bomb.BOMBS.append(self) 

    @classmethod
    def get_bombs(cls):
        return [str(bomb) for bomb in cls.BOMBS]

    def __str__(self):
        return f"({self.x}, {self.y})"


b1 = Bomb(1, 1)
# str([])
print(Bomb.BOMBS)
b2 = Bomb(2, 2)
print(Bomb.BOMBS)
print(Bomb.get_bombs())