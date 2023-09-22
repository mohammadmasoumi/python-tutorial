
class Student:
    def __init__(self, name, avg):
        self.name = name
        self.avg = avg
        # we can have prop that it's value doesn't come from params
        self.degree = 'Design of Algo'


abbasi = Student(name='abbasi', avg=60)
karkehabadi = Student(name='karkehabadi', avg=40)

# access - read property value
print(karkehabadi.avg)

# update - update property value
karkehabadi.avg = 100
print(karkehabadi.avg)

# leak information
# unwanted changes in props values

# delete - delete a property
# AttributeError: 'Student' object has no attribute 'avg'
del karkehabadi.avg
print(karkehabadi.avg)
