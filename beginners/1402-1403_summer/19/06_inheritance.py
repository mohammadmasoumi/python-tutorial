
class Bird:

    def fly(self):
        print("I'm flying")


# class ClassName(Parent)
class Parrot(Bird):
    pass


class Rooster(Bird):

    # override fly behaviour in ChildClass `Rooster`
    def fly(self):
        print("I can't fly, such a pity!")


casco = Parrot()
# - Search in Parrot for fly behaviour
# - Search parent of Parrent: Bird
# - Search in python Object class
# - raise AttributeError: doesn't have this property
lari = Rooster()

# AttributeError: 'Parrot' object has no attribute 'walk'
# casco.walk()
casco.fly()
lari.fly()

# method resolution order
print(Rooster.mro())
