# inheritance

"""
        Animal

Mamals  Birds Reptiles ...

"""


class Bird:
    species = "birds-gan"

    def __init__(self, name, habitant, can_fly):
        self.name = name
        self.habitant = habitant
        self.can_fly = can_fly


class Parrot(Bird):

    def __init__(self, name, habitant):
        # call parent methods
        super().__init__(name, habitant, can_fly=True)


blue = Parrot(name="blue", habitant="forest")

# method resolution order(MRO)
# blue.name
# mro: Parrot
#
# blue.habitant
# mro: Parrot
#
# blue.can_fly
# mro: Parrot -> the most left parrent (Bird)

print(blue.name, blue.habitant, blue.can_fly)

print(Parrot.__mro__)
# (<class '__main__.Parrot'>, <class '__main__.Bird'>, <class 'object'>)
