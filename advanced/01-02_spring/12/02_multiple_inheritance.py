
class A:

    def __init__(self, roll):
        self.roll = roll


class C:

    def __init__(self, room):
        self.room = room


class B(A, C):

    def __init__(self, name) :
        self.name = name

        # TypeError: A.__init__() got an unexpected keyword argument 'room'
        # super().__init__(roll="manager", room=1)
        # super().__init__(roll="manager")
        A.__init__(self, roll="manager")
        C.__init__(self, room=1)

        # super(A, self).__init__(roll="manager")
        # super(C, self).__init__(room=1)

        # super().__init__(roll="manager")
        # super().__init__(roll=roll)



instance = B('asghar')
# roll = "manager"
print(instance.name)
# AttributeError: 'B' object has no attribute 'roll'
print(instance.roll)
print(instance.room)