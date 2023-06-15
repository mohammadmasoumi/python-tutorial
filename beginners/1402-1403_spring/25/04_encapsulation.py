class Student:
    def __init__(self, name, scores):
        self.name = name
        self.__scores = scores  # private
        # _ convension
        # _property_name -> private
        # accessable
        # _ or __

    @property
    def grade(self):
        return sum(self.__scores) // len(self.__scores)


imani = Student("imani", [20, 20, 20, 20])
hassan = Student("eskandari", [19, 19, 19, 19])
mahdi = Student("mahdi", [10, 10, 10, 10, 10])

# private
# set, get, del
# mahdi.__scores = [22, 22, 22, 22]
# AttributeError: 'Student' object has no attribute '__scores'
# print(mahdi.__scores)

print(mahdi.grade)
print("belt")
