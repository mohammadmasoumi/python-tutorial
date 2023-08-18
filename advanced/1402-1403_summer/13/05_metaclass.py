

# __call__ 
#   self = __new__
#   __init__(self)

class MyMetaClass(type):

    def __new__(cls, name, bases, props):
        instance = super().__new__(cls, f"Asghar{name}", bases, props)

        print(f"class name: {instance.__name__}")

        return instance


class Student(metaclass=MyMetaClass):

    def __init__(self, family) :
        self.family = family


# Student -> name: AsgharStudent
# 1.
student = Student(family='asghari')
print(student.family)
print(Student.__name__)

# 2.
# student = AsgharStudent(family='asghari')
# print(student.family)

