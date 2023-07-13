
class Bomb:
    # Shared between instances
    # ------ class property
    BOMBS = []

    # ------

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.BOMBS = []

        print(f"BOMBS: {id(self.BOMBS)}")

        self.BOMBS.append(self)


b1 = Bomb(10, 10)
print(b1.BOMBS)

b2 = Bomb(5, 5)
print(b2.BOMBS)


# -------------
