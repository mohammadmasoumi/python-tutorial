# Enemy

# bow
# spare


class Soldier:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

    def speak(self):
        print("Speakinnnnnnnnnnnnnnng")

    def attack(self, soldier):
        soldier.hp -= self.damage


class Bowman(Soldier):
    def __init__(self, hp, damage, rang):
        super().__init__(hp, damage)
        self.rang = rang

    def speak(self):
        print("Bowman start to speak")
        super().speak()


class Spareman(Soldier):
    def __init__(self, hp, damage, spare_length):
        super().__init__(hp, damage)
        self.spare_length = spare_length
