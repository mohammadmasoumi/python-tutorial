class Student:
    def __init__(self, name, scores):
        self.name = name
        self.__scores = scores

    @property
    def scores(self):
        return self.__scores

    @scores.setter
    def scores(self, new_scores):
        self.__scores = new_scores

    @scores.deleter
    def scores(self):
        self.__scores.clear()

    @property
    def avg(self):
        return sum(self.__scores) // len(self.__scores) 

name_student_mapping = {}

for _ in range(int(input())):
    name, *scores = input().split()
    name_student_mapping[name] = Student(
        name=name, 
        scores=list(map(int, scores))
    )


std_name = input()
std_instance = name_student_mapping.get(name)

if std_instance:
    print(std_instance.avg)
else:
    print("Student does not exist.")
