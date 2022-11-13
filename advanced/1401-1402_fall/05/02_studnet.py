#
class Student:

    def __init__(self, name) -> None:
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    @property
    def avg(self):
        # s = sum.scores
        # avg = s // len(scores)
        return sum(self.scores)//len(self.scores)


std1 = Student("mina")
print(std1.name)
# add_score(std1, 10)
std1.add_score(10)

std2 = Student("amir")
print(std2.name)
# add_score(std2, 10)
std2.add_score(20)
print(std2.avg)
