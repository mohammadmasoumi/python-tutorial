
# convention
# 1. camelCaseCase
# 2. snake_case
# 3. PascalCase

# blueprint
# طرح واره
class Student:
    # constructor

    # __function__
    # magic function or dunder method

    # typing
    # variable_name: variable_type = default_value
    def __init__(self, name: str, age: int, grade: float, is_disabled: bool = False) -> None:  # returnt type
        """This is a constructor of Student class

        Args:
            name (str): _description_
            age (int): _description_
            grade (float): _description_
            is_disabled (bool, optional): _description_. Defaults to False.
        """
        # self: current object
        # return type must be NONE

        # self.[attr] = value
        # self.name = name
        self.firstname: str = name
        self.lastname: int = age
        # self.firstname = name

        # self.name = name
        self.age = age
        self.grade = grade
        self.is_disabled = is_disabled
        self.courses = []
        self.is_processed = False

    # cast 2 str
    def __str__(self) -> str:
        return f"{self.firstname}-{self.age}-{self.grade}-{self.is_disabled}"

    def __int__(self) -> int:
        return self.age

    # comparison operator
    # > < >= <= == !=
    def __ge__(self, obj) -> bool:
        # greater than equal
        # [WRONG] isinstance(obj, str) or isinstance(obj, int) or ...
        # if isinstance(obj, (Student, int, str))
        if isinstance(obj, Student):
            return self.grade >= obj.grade

        elif isinstance(obj, (int, str, float, list, tuple)):
            raise ValueError(f"{type(self)} can't comparison to {type(obj)}")

        # return None


a = 12
b = "helloworld"
c = [1, 2, 3]


# instanciation
# instance
std1 = Student(name="gholi", age=22, grade=11, is_disabled=True)
std2 = Student(name="gholi007", age=22, grade=12, is_disabled=True)


# std1.__ge__(std2)
print(std1 >= std2)
# std1.__ge__(12)
# print(std1 >= 12)
# std1.__ge__("hassan")
# print(std1 >= "hassan")

# "hassan".__ge__(std1)
# TypeError: '>=' not supported between instances of 'str' and 'Student'
print("hassan" >= std1)

# self: student
# variable_name.[property]

# 1. Access
print(std1.firstname, std2.firstname)
print(std1.is_disabled, std2.is_disabled)

# 2. Update
# std1 = self.name
# std1.name = "gholi0022"
std1.firstname = "gholi0022"
print(std1.firstname, std2.firstname)
std1.age = 23
print(f"{std1.firstname} is {std1.age} years old.")

# 3. Delete
# del std1.firstname
# AttributeError: 'Student' object has no attribute 'firstname'
# print(f"{std1.firstname} is {std1.age} years old.")

# <__main__.Student object at 0x0000014E466B2D90>
# behind the scene
# print(std1) -> str(std1) -> print in terminal
print(std1)
print(std2)
cast_2_str = str(std1)
# std1.__str__()
print(cast_2_str)

print(int(std1))
print(int(std2))
