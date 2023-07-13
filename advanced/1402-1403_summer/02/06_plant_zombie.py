
class AttackConfig:

    def __init__(self, damage, attack_speed, rng):
        self.range = rng
        self.damage = damage
        self.attack_speed = attack_speed


# attack_config = {
#     "range":  rng,
#     "damage":  damage,
#     "attack_speed":  attack_speed,
# }


class Creature:

    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp


class Plant(Creature):

    def __init__(self, x, y, hp, attack_config):
        self.attack_cfg = attack_config
        super().__init__(x, y, hp)


class DoublePlant(Plant):
    def __init__(self, x, y):
        attack_config = AttackConfig(
            damage=15,
            attack_speed=200,
            range=3
        )
        hp = 80
        super().__init__(x, y, hp, attack_config)


class SinglePlant(Plant):

    def __init__(self, x, y):
        attack_config = AttackConfig(
            damage=20,
            attack_speed=100,
            range=4
        )
        hp = 100
        super().__init__(x, y, hp, attack_config)


class MovableCreature(Creature):

    def __init__(self, x, y, hp, move_speed):
        self.move_speed = move_speed
        super().__init__(x, y, hp)


class Enemy(MovableCreature):

    def __init__(self, x, y, hp, move_speed, attack_config):
        self.attack_cfg = attack_config
        self.move_speed = move_speed
        super().__init__(x, y, hp)


class SavageEnemy(Enemy):

    def __init__(self, x, y):
        attack_config = AttackConfig(
            range=1,
            damage=10,
            attack_speed=100
        )
        hp = 100
        move_speed = 50
        super().__init__(x, y, hp, move_speed, attack_config)


class CoolEnemy(Enemy):

    def __init__(self, x, y):
        attack_config = AttackConfig(
            range=1,
            damage=5,
            attack_speed=200
        )
        hp = 300
        move_speed = 100
        super().__init__(x, y, hp, move_speed, attack_config)
