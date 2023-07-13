"""
            property
    instance  
            behaviour

            property
    class 
            behaviour
"""


class Bomb:
    BOMBS = []

    def __init__(self, damage):
        self.damage = damage

        # self.BOMBS.append(self)
        Bomb.BOMBS.append(self)

    @classmethod
    def get_bombs(cls):  # cls: Bomb
        # Bomb.BOMBS
        return cls.BOMBS


# instance
b1 = Bomb(damage=100)
# print(b1.BOMBS)

b2 = Bomb(damage=200)
# print(b1.BOMBS)
# print(b2.BOMBS)

# class property
print(Bomb.BOMBS)
print(Bomb.get_bombs())
