import time
import random


CELL_WIDTH = 11
my_map = None


class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__contents = []

    @property
    def contents(self):
        return self.__contents

    def add_content(self, obj):
        self.__contents.append(obj)
    
    def remove_content(self, obj):
        self.__contents.remove(obj)
    
    def __str__(self):
        return "-".join(map(str, self.__contents)).center(CELL_WIDTH)


# cell = Cell(10, 10)
# cell.add_content(12)
# print(cell)

class Map:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.__board = [[Cell(x=col, y=row) for col in range(self.width)] for row in range(self.length)]

    @property
    def board(self):
        return self.__board

    def add_content(self, obj, x, y):
        # Cell: self.board[y][x]
        self.__board[y][x].add_content(obj)

    def remove_content(self, obj, x, y):
        # Cell: self.board[y][x]
        self.__board[y][x].remove_content(obj)

    def print_map(self):
        # [Cell, Cell, Cell]
        """
        (11 + 1) * self.width + 1
        -----------------------------
        |      |      |      |      |
        -----------------------------
        """
        roof = (CELL_WIDTH + 1) * self.width + 1

        for row in self.__board:
            print("-" * roof)
            print("|" + "|".join(map(str, row)) + "|")

        print("-" * roof)


class Zombie:
    
    def __init__(self, x, y, hp, damage, speed):
        self.x = x
        self.y= y
        self.hp = hp
        self.damage = damage
        self.speed = speed

    def move(self):
        global my_map

        new_x = self.x - 1

        if 0 <= new_x < my_map.width:
            my_map.remove_content(self, self.x, self.y)
            self.x = new_x
            my_map.add_content(self, self.x, self.y)

    def reduce_hp(self, damage):
        global my_map

        self.hp -= damage
        print(f"Akhhhhhhhhhhhhhhhhhhhhhhhhhhh {self.hp} {damage}")

        if self.hp <= 0:
            my_map.remove_content(self, self.x, self.y)


class SlowZombie(Zombie):

    def __init__(self, x, y):
        hp = 100
        damage = 50
        speed = 1

        super().__init__(x, y, hp, damage, speed)

    def __str__(self):
        return "SZ"
    

class FastZombie(Zombie):

    def __init__(self, x, y):
        hp = 50
        damage = 100
        speed = 1

        super().__init__(x, y, hp, damage, speed)

    def __str__(self):
        return f"FZ"


class Bullet:

    def __init__(self, x, y, damage, speed):
        global my_map

        self.x = x
        self.y = y 
        self.damage = damage
        self.speed = speed

        my_map.add_content(self, self.x, self.y)

    def move(self):
        global my_map

        new_x = self.x + 1

        if 0 <= new_x < my_map.width:
            my_map.remove_content(self, self.x, self.y)
            self.x = new_x
            my_map.add_content(self, self.x, self.y)
        else:
            my_map.remove_content(self, self.x, self.y)


    def check_zombie(self):
        global my_map

        cell = my_map.board[self.y][self.x]

        for obj in cell.contents:
            if isinstance(obj, (SlowZombie, FastZombie)):
                obj.reduce_hp(self.damage)
                my_map.remove_content(self, self.x, self.y)
                return True

    def __str__(self):
        return "B"


class Flower:

    def __init__(self, x, y, hp, damage, fire_rate, fire_range, fire_speed):
        self.x = x
        self.y = y
        self.hp = hp 
        self.damage = damage
        self.fire_rate = fire_rate
        self.fire_range = fire_range
        self.fire_speed = fire_speed

    def shoot(self):
        global my_map

        """
        F B   Z  |
        """
        # fire_range: 4 | 0 ... 3
        # x: 2, y: 2, fire_range: 4
        # (2,2), (3,2), (4,2), (5,2), (6,2) 
        # 2, 2 + 4 + 1
        for new_x in range(self.x, self.x + self.fire_range + 1):
            if 0 <= new_x < my_map.width:
                # Cell: my_map.board[self.y][new_x]
                # Cell.contents
                for obj in my_map.board[self.y][new_x].contents:
                    if isinstance(obj, (SlowZombie, FastZombie)):
                        return Bullet(self.x, self.y, self.damage, self.fire_speed)
                        

    def plant(self):
        global my_map
        my_map.add_content(self, self.x, self.y)

    def destroy(self):
        # TODO: check this part later
        # global my_map
        # my_map.remove_content(self, self.x, self.y)
        pass


class SlowFlower(Flower):

    def __init__(self, x, y):
        hp = 100
        damage = 20
        fire_rate = 1
        fire_range = 10
        fire_speed = 1
        super().__init__(x, y, hp, damage, fire_rate, fire_range, fire_speed)
    
    def __str__(self):
        return "SF"


class FastFlower(Flower):

    def __init__(self, x, y):
        hp = 50
        damage = 40
        fire_rate = 2
        fire_range = 5
        fire_speed = 1
        super().__init__(x, y, hp, damage, fire_rate, fire_range, fire_speed)
    
    def __str__(self):
        return "FF"


class Engine:

    def __init__(self):
        self.rnd = 0
        self.bullets = []

    def run(self):
        global my_map

        my_map = Map(10, 10)
        zombies_rounds = {
            2: [
                SlowZombie(
                   9, 0
                ),
                # FastZombie(
                #     x=my_map.width - 1, 
                #     y=random.randint(0, my_map.length - 1), 
                # )
            ]
        }

        flowers_rounds = {
            1: [
                SlowFlower(
                   0, 0 
                ),
                # SlowFlower(
                #     x=random.randint(0, my_map.length - 1), 
                #     y=random.randint(0, my_map.length - 1), 
                # ),
                # SlowFlower(
                #     x=random.randint(0, my_map.length - 1), 
                #     y=random.randint(0, my_map.length - 1), 
                # ),
                # FastFlower(
                #     x=random.randint(0, my_map.length - 1), 
                #     y=random.randint(0, my_map.length - 1), 
                # ),
                # FastFlower(
                #     x=random.randint(0, my_map.length - 1), 
                #     y=random.randint(0, my_map.length - 1), 
                # )
            ]
        }

        while True:
            time.sleep(2)
            print(f"--------------------------------------- {self.rnd} ---------------------------------------")

            for row in my_map.board: # h
                for cell in row: # w
                    for obj in cell.contents: # n
                        # O(h*w*n)
                        # speed: 2 slow
                        # speed: 1 fast
                        # rnd 
                        if isinstance(obj, (SlowFlower, FastFlower)) and self.rnd % obj.fire_rate == 0:
                            bullet = obj.shoot()
                            if bullet:
                                self.bullets.append(bullet)

            my_map.print_map()

            # for row in my_map.board: # h
            #     for cell in row: # w
            #         for obj in cell.contents: # n
            #             # print(f"obj: {obj.x} {obj.y} {obj}")
            #             if isinstance(obj, (Bullet, )) and self.rnd % obj.speed == 0:
            #                 my_map.print_map()
            #                 obj.move()
            for bullet in self.bullets:
                if self.rnd % bullet.speed == 0:
                    bullet.move()
                    if bullet.check_zombie():
                        self.bullets.remove(bullet)

            for row in my_map.board: # h
                for cell in row: # w
                    for obj in cell.contents: # n
                        # O(h*w*n)
                        # speed: 2 slow
                        # speed: 1 fast
                        # rnd 
                        if isinstance(obj, (SlowZombie, FastZombie)) and self.rnd % obj.speed == 0:
                            obj.move()


            for zombie in zombies_rounds.get(self.rnd, []):
                # obj, x, y
                my_map.add_content(zombie, zombie.x, zombie.y)

            for flower in flowers_rounds.get(self.rnd, []):
                # obj, x, y
                flower.plant()

            self.rnd += 1

            if self.rnd == 100:
                break



engine = Engine()
engine.run()