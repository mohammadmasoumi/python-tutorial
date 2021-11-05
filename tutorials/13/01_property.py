class Student:

    def __init__(self, name):
        self._name = name

    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    
    @name.deleter
    def name(self):
        del self._name


student = Student("Jack")
print(student.name)
student.name = "Asghar"
print(student.name)
del student.name
