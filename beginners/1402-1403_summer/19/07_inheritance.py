

class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying.")


# class ClassName(Parent)
class Parrot(Bird):
    pass


class Roster(Bird):

    def __init__(self, name, _type):
        self._type = _type

        # super().behaviour_name_in_parent()
        super().__init__(name)

    # override fly behaviour in ChildClass `Roster`
    def fly(self):
        print("I can't fly, such a pity!")


casco = Parrot()
# - Search in Parrot for fly behaviour
# - Search parent of Parrent: Bird
# - Search in python Object
# - raise AttributeError: doesn't have this property
lari = Roster()

# AttributeError: 'Parrot' object has no attribute 'walk'
# casco.walk()
casco.fly()
lari.fly()
