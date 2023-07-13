# instance level property
"""
    BOMBS
b1 -> [] 344

    BOMBS
b2 -> [] 424

"""


class Bomb:

    def __init__(self, x, y):
        # instance level property
        # self: b1
        # b1.x = x
        # b1.y = y
        # b1.BOMBS = [b1]
        # -------
        # self: b2
        # b2.x = x
        # b2.y = y
        # b2.BOMBS = [b2]
        self.x = x
        self.y = y
        self.BOMBS = []
        print(f"BOMBS: {id(self.BOMBS)}")

        self.BOMBS.append(self)


b1 = Bomb(10, 10)  # BOMBS: [b1]
# Bomb.__init__(b1, 10, 10)
print(b1.BOMBS)

b2 = Bomb(5, 5)  # BOMBS: [b2]
# Bomb.__init__(b2, 5, 5)
print(b2.BOMBS)
