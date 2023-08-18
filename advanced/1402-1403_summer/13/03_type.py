# type
a = 12
print(type(a))

# type(object) -> the object's type type(name, bases, dict, **kwds) -> a new type
# type: metaclass
# metaclass is responsible for creating classes
# metaclass -> create classes

# class Student:
#     pass

# __dict__ store class/instance props and behaviour
A = type("A", (), {'a': 12})
B = type("B", (A,), {"a": 13})
C = type("C", (B, A), {"a": 14})

# class A:
#     a = 12

# class B(A):
#     a = 13

# class C(B, A):
#     a = 14

print(C.__mro__) # CBAO

c = C()
print(c.a)

classes = []
for i in range(10):
    cls = type(f"A{i}", (), {"a": i+1})
    classes.append(cls)

for cls in classes:
    print(cls.__name__, cls().a)

# -----------
# class Student:
#     STUDENTS = []
#     def __init__(self, name):
#         self.name = name
#         Student.STUDENTS.append(self)

#     @classmethod
#     def get_students(cls):
#         return cls.STUDENTS


STUDENTS = []
def __init__(self, name):
    self.name = name
    STUDENTS.append(self)

@classmethod
def get_student(cls):
    return cls.STUDENTS

# create class | metaclass
Student = type("Student", (), {
    '__init__': __init__,
    'STUDENTS': STUDENTS,
    'get_student': get_student
})

s = Student(name="jadidi")
print(s.name)
print(Student.get_student())

# -------------

AsgharAgha = type('Asghar', (), {'a': 12})
class Asghar:
    a = 13


print(id(AsgharAgha), id(Asghar))

asghar_instance = Asghar()
print(asghar_instance.a)

# names
print(Asghar.__name__)
print(AsgharAgha.__name__)