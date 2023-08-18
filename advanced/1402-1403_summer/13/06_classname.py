
class Student:
    __name__ = "AsgharStudent"
    __qualname__ = "AsgharStudent"

s = Student()
print(Student.__name__) # Student
print(s.__class__.__name__) # Student

# Student class
# s instance

# s.__class__: Student
# s.__class__.__name__ == Student.__name__ 

s2 = s.__class__() # Student() == s.__class__()
print(s, s2)