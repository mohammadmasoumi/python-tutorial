# from classproperty import classproperty


class Bomb:
    # ------ class property
    BOMBS = []

    # ------

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.BOMBS = []

        print(f"BOMBS: {id(self.BOMBS)}")
        # self => Bomb
        Bomb.BOMBS.append(self)

    @classproperty
    def add():
        pass

    @classmethod
    def get_bombs(cls):
        # Bomb.BOMBS
        # cls: Bomb
        return cls.BOMBS


b1 = Bomb(10, 10)
# print(Bomb.BOMBS)
print(Bomb.get_bombs())
print(b1.get_bombs())  # DO NOT USE IT

b2 = Bomb(5, 5)
# print(Bomb.BOMBS)
print(Bomb.get_bombs())
print(b2.get_bombs())  # DO NOT TRY THIS IN YOUR CODE
