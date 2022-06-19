
class A:

    def __init__(self, roll):
        self.roll = roll

class B(A):

    def __init__(self, name) :
        self.name = name
        super().__init__(roll="manager")
        # super().__init__(roll=roll)


instance = B('asghar')
# roll = "manager"
print(instance.name)
# AttributeError: 'B' object has no attribute 'roll'
print(instance.roll)