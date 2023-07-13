# Abstract
# Abstraction
from abc import ABC, abstractmethod

# Abstract
# Concrete


class EnemyAbstract(ABC):

    def __init__(self, x, y, hp):
        pass

    @abstractmethod
    def attack(self):
        pass

# Wrong
# instance = EnemyAbstract()


class Enemy(EnemyAbstract):

    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp

    # def attack(self):
    #     pass

    def shoot(self):
        self.attack()


class KhafanEnemy(Enemy):

    def __init__(self, x, y, hp, gun):
        self.gun = gun
        super().__init__(x, y, hp)

    def attack(self):
        print(f"I am attacking with {self.gun}")


class GheirKhafanEnemy(Enemy):

    def __init__(self, x, y, hp, knife):
        self.knife = knife
        super().__init__(x, y, hp)

    # def attack(self):
    #     print(f"I am attacking with {self.knife}")
