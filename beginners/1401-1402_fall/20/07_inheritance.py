# Inheritance

#   Creature
# Birds     Reptiles

class Creature:

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos

    # method 2
    def crawl(self):
        if isinstance(self, Birds):
            raise NotImplementedError()

        print(f"{self.name} is crawling ...")

    def move(self):
        self.pos += 1
        # print(f"{self.name} is moving ...")

    def __str__(self):
        return self.name


class Reptiles(Creature):

    # def __init__(self, name):
    #     self.name = name

    def move(self):
        super().move()
        print(f"{self.name} is crawling {self.pos} ...")

    def crawl(self):
        print(f"{self.name} is crawling ...")

    # def __str__(self):
    #     return self.name


class Birds(Creature):

    # def __init__(self, name):
    #     self.name = name

    def move(self):
        super().move()
        print(f"{self.name} is flying to {self.pos} ...")
        # super().move()

    def fly(self):
        print(f"{self.name} is flying ...")

    # override
    # method 1
    def crawl(self):
        raise NotImplementedError()

    # def __str__(self):
    #     return self.name


snake = Reptiles(name="python", pos=0)
print(snake)
# mro = method resolution order
print(snake.name)
snake.move()
snake.crawl()
bird = Birds(name="dab", pos=1)
print(bird)
bird.move()
bird.crawl()
