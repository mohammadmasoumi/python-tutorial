"""
Car

Cell
    contents: [🚒, 🚑]

Street
    [🚒, 🚑][][C][][][C][][][][][][][][][][][][]

# windows + . => emoji

[][][*][*][*]
[][][][][*]
[][][][][*]
[][][][][*]
[][][][][*]
"""
import keyboard
import time


class Car:

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos

        # shohada_street: Street
        # shohada_street.road: list
        # shohada_street.road[0]: Cell

        shohada_street.road[self.pos].add_content(self)

    def move(self, direction):
        # forward., backward

        if direction == "d":
            if self.pos + 1 < shohada_street.length:
                shohada_street.road[self.pos].remove_content(self)
                self.pos += 1
                shohada_street.road[self.pos].add_content(self)
            else:
                print("Invalid direction!")

        elif direction == "a":
            if 0 <= self.pos - 1:
                shohada_street.road[self.pos].remove_content(self)
                self.pos -= 1
                shohada_street.road[self.pos].add_content(self)
            else:
                print("Invalid direction!")

    def __str__(self):
        return self.name


class Cell:

    def __init__(self, pos):
        self.pos = pos
        self.contents = []

    def add_content(self, element):
        self.contents.append(element)

    def remove_content(self, element):
        self.contents.remove(element)

    def __str__(self):
        return " ".join([str(content) for content in self.contents]).center(10)


class Street:

    def __init__(self, name, length):

        self.name = name
        self.length = length
        self.road = [Cell(pos=i) for i in range(length)]
        # [i for i in range(length)]

        # road = []
        # for i in range(length):
        #     road.append(Cell(pos=i))

    def __str__(self):
        #      20         20       20        20
        # | 🚒, 🚑 |         |         |     🚑    |
        return f'|{"|".join([str(cell) for cell in self.road])}|'


class Engine:

    def __init__(self, rnd):
        self.rnd = rnd

    # def instanciate(self):

    def run(self):
        global shohada_street

        shohada_street = Street("shohada", 9)

        # car_name = input("Car name: ")
        car = Car("🏍", 0)

        cars = [
            Car("🚒", 0),
            car,
            Car("🚎", 0),
            Car("🛺", 0),
            Car("🚑", 1),
            Car("🦼", 2)
        ]

        counter = 0
        while True:
            time.sleep(1)

            if counter == self.rnd:
                break

            print(f"\r{shohada_street}", end="")
            # direction = input("\nPlease enter dicretion: ")
            # if keyboard.is_pressed("d"):
            # for car in cars:
            #     if car.name == name:
            car.move(direction="d")
            # elif keyboard.is_pressed("a"):
            #     car.move(direction="a")


engine = Engine(8)
engine.run()
