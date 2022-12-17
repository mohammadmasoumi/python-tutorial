# name

class Student:

    def __init__(self, name):

        self.name = name
        # private
        self.__scores = []

    # get __score
    # set [score, score] => 0 < score < 20
    # del clear

    @property
    def scores(self):
        return self.__scores

    @scores.setter
    def scores(self, scores):
        # self.__scores = [score for score in scores if 0 <= score <= 20]
        for score in scores:
            if not (0 <= score <= 20):
                return

        self.__scores = scores
        # return None

    @scores.deleter
    def scores(self):
        self.__scores.clear()


std1 = Student(name="ali")
print(std1.scores)
std1.scores = [20, 19, 20]
print(std1.scores)
del std1.scores
print(std1.scores)
