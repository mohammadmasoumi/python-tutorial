class Student:

    def __init__(self, name):
        self.name = name
        # private
        self.__scores = []
        self._scores2 = []

    @property
    def marks(self):
        # check permission
        return self.__scores

    @marks.setter
    def marks(self, new_scores):
        for score in new_scores:
            if not (0 <= score <= 20):
                print("Invalid scores")
                return

        self.__scores = new_scores

    @marks.deleter
    def marks(self):
        self.__scores.clear()

    @property
    def avg(self):
        average = sum(self.__scores) / len(self.__scores)
        return f"{average:.2f}"


"""
name
marks
"""

std1 = Student(name="mina")
# AttributeError: 'Student' object has no attribute '__scores'
print(std1._scores2)
# getter
print(std1.marks)  # access
# print(std1.__scores)

# std1.scores = [22, 22, 22]

# setter
std1.marks = [20, 19, 20]
print(std1.marks)

std1.marks = [20, 19, 22]
print(std1.marks)

# deletter
# del std1.name
# AttributeError: 'Student' object has no attribute 'name'
# print(std1.name)

del std1.marks
print(std1.marks)

# getter
# setter

# private
# __scores
# print(std1.scores)
# std1.scores = [22, 22, 29]

#  [virtual/proxy property] => __scores
# Me => asghar => __scores
