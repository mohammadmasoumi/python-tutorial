class Student:
    def __init__(self, name):
        self.name = name
        self.__scores = []

    @property
    def scores(self):
        return self.__scores

    # setter -> get new list and assign to the __scores
    # deleter -> clear

    @scores.setter
    def scores(self, new_scores):
        # search for specific item in list -> for-else
        for score in new_scores:
            if not (0 <= score <= 20):
                break
        else:
            self.__scores.extend(new_scores)

    @scores.deleter
    def scores(self):
        self.__scores.clear()


std1 = Student(name="ali")
std1.scores = [21, 1, 10]
print(std1.scores)
std1.scores = [20, 20, 10]
print(std1.scores)
# AttributeError: property 'scores' of 'Student' object has no deleter
del std1.scores
print(std1.scores)
