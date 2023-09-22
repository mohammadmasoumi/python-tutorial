
class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying.")


class Parrot(Bird):
    pass


class Roster(Bird):

    def __init__(self, name, _type):
        self._type = _type
        super().__init__(name)

    def fly(self):
        super().fly()
        print("I can't fly, such a pity!")
