import functools


# 3

def run_twice(func):
    # *args, **kwargs
    # def wrapper(instance, *args, **kwargs):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # self: student
        print(dir(self))
        print(id(self))

        bye_method = getattr(self, "bye")
        print(f"args: {args}, kwargs: {kwargs}")

        self.set_name("Ahmad")

        func(self, *args, **kwargs)
        func(self, *args, **kwargs)

        bye_method()

    return wrapper


class Student:

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    @run_twice
    def greeting(self, another_student):
        print(f"Hello, I am {self._name}. Nice to meet you Mr/Mrs {another_student.get_name()}")

    def bye(self):
        print("Bye")


student1 = Student(name="Ali")
student2 = Student(name="Asghar")

student1.bye()  # now self is student1
# bye(student1)

student2.bye()  # now self is student2
# bye(student2)

student1.greeting(student2)
print(id(student1))
print(student1.get_name())
# print(id(student1))
