
class Student:

    def __init__(self, name):
        self.__name = name
        self.__scores = []

    @property
    def scores(self):
        return self.__scores

    # AttributeError: can't set attribute 'scores'
    @scores.setter
    def scores(self, new_value):
        self.__scores.extend(new_value)

    @scores.deleter
    def scores(self):
        self.__scores.clear()

    def __delattr__(self, __name: str):
        print(f"Called __delattr__")

        if __name == "name":
            pass


std1 = Student("hasan")
print(std1.scores)
# AttributeError: can't set attribute 'scores'
std1.scores = [20, 19]
std1.scores = [17, 18]
print(std1.scores)
# AttributeError: can't delete attribute 'scores'
del std1.scores
print(std1.scores)
