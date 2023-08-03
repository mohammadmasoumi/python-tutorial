
class Bomb:
    # class property
    BOMBS = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

        # BOMBS: class property
        Bomb.BOMBS.append(self)

    # behaviour
    # method
    @classmethod
    def get_bombs(cls):
        return [str(bomb) for bomb in cls.BOMBS]

    def __str__(self):
        return "B"


b1 = Bomb(10, 10)
b2 = Bomb(10, 10)
#
print(b2.BOMBS) # BAD PRACTICE

print(Bomb.get_bombs())