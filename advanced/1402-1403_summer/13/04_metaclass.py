

# __call__ 
#   self = __new__
#   __init__(self)

class MyMetaClass(type):

    def __new__(cls, name, bases, props):
        print(f"name: {name}")
        print(f"bases: {bases}")
        print(f"props: {props}")

        instance = super().__new__(cls, name, bases, props)

        print(f"instance: {instance}")
        print(f"instance name: {instance.__name__}")

        # inject props
        instance.name = "asghar"
        instance.age = 22
        instance.height = 180

        return instance


class Student(metaclass=MyMetaClass):
    # name = "asghar"
    # age = 22
    # height = 180

    def __init__(self, family) :
        self.family = family


student = Student(family='asghari')
print(student.family)
print(student.name)
