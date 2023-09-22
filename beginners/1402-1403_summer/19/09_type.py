
class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(type(self))
        print(f"{self.name} is flying.")


class Parrot(Bird):
    pass


class Rooster(Bird):

    def __init__(self, name, _type):
        self._type = _type
        super().__init__(name)

    def fly(self):
        super().fly()
        print("I can't fly, such a pity!")


james = Rooster('james', 'james-type')
# print(type(james))
# print(isinstance(james, Rooster))
james.fly()

birdy = Bird('birdy')
birdy.fly()

#
# my_list = []
# my_list.append()  # `append` behaviour


# class MyList:
#     def __init__(self):
#         self.__container = []

#     def append(self, item):
#         self.__container.append(item)
