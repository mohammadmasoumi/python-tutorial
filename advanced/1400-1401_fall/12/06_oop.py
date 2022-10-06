# class Pascal Case
# MyStudent - PascalCase
# myNameIs - camelCase
# my_student - snake case

class Student:

    # constructor
    def __init__(self, name, age, gender):
        """
        Student Constructor

        @todo:
        @note:
        :exception : Warning be caution

        :param name: student name
        :type name: str
        :param age:  student age
        :type age: int
        :param gender: student age
        :type gender: str
        """
        # instance properties
        self.name = name
        self._age = age
        self.__gender = gender
        self._scores = []

    # more control on properties
    def set_scores(self, score: int):
        """

        :param score:
        :return:
        """
        self._scores.append(score)

    def get_scores(self):
        """

        :return:
        """
        return self._scores

    # behavior
    def grow_up(self, age=1):
        """

        :param age:
        :return:
        """
        self._age += age

    def is_male(self):
        """

        :return:
        """
        return True if self.__gender == "male" else False


student1 = Student("Ali", 20, "male")
student2 = Student("arezo", 29, "female")

print(f"name: {student1.name}")
print(f"age: {student1._age}")
# student1._age = 30
# print(student1._age)
student1.grow_up()
student1.grow_up(5)
print(f"age: {student1._age}")
student1.set_scores(20)
student1.set_scores(19)
student1.set_scores(10)
print(student1.get_scores())
print(student1.is_male())

#
print(student2.get_scores())
print(student2.is_male())

# print(Student.__doc__)

# print(f"student1: {student1}")
# print(f"student2: {student2}")

# class M:
#     def __init__(self):
#
