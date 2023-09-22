
# property
# - access - getter
# - update - setter
# - delete - deleter

class Student:
    def __init__(self, name, avg):
        self.name = name
        # private property
        self.__avg = avg  # you can't access to it
        # self._avg = avg  # convention - you can access to it but you mustn't
        self.degree = 'Design of Algo'

    # define a new virtual property
    # define secretoty
    # access
    @property
    def avg(self):
        # logic
        return self.__avg

    # update
    @avg.setter
    def avg(self, new_value):
        if 0 <= new_value <= 100:
            self.__avg = new_value

    # delete
    @avg.deleter
    def avg(self):
        self.__avg = 0


karkehabadi = Student(name='karkehabadi', avg=40)  # instatiation
# AttributeError: 'Student' object has no attribute '__avg'
# print(karkehabadi.__avg)
# print(karkehabadi._avg)

# karkehabadi.__avg = 100
# print(karkehabadi.__avg)

print(karkehabadi.avg)  # call getter - property
karkehabadi.avg = 120  # call setter
print(karkehabadi.avg)  # call getter - property
karkehabadi.avg = 100  # call setter
print(karkehabadi.avg)  # call getter - property
del karkehabadi.avg  # call deleter
print(karkehabadi.avg)  # call getter - property
