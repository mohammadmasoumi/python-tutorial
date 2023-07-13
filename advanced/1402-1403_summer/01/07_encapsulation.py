
class Student:

    def __init__(self, name, scores):
        self.name = name
        # private - convension
        # self._scores = scores
        # self.__scores
        self.__scores = scores

    @property
    def scores(self):
        # instance -> scores -> __scores
        # instance -/-> __scores [by making __scores private]

        # get
        # print(std1.scores)
        if self.name == "imani":  # "sabour"
            return []

        return self.__scores

    @scores.setter
    def scores(self, new_scores):
        # set
        # std1.scores = [20, 20, 20]

        # if all([0 <= value <= 20 for value in new_scores]):
        #     self.__scores = new_scores
        # else:
        #     print("got invalid scores.")

        print("you can't change scores.")

    @scores.deleter
    def scores(self):
        self.__scores.clear()

    def grade(self):
        return sum(self.__scores) / len(self.__scores)


# std1 = Student(name="imani", scores=[17, 20, 12, 19])
# # std1
# print(std1.grade())

# AttributeError: 'Student' object has no attribute '__scores'
# print(std1.__scores)

# unwanted update properties
# Mother
# std1.__scores = [20, 20, 20, 20]
# print(std1.grade())

# Father - 0 <= score <= 20
# std1.__scores = [22, 22, 22, 22]
# print(std1.grade())

# property
# - access - get
# - update - set
# - delete - del


"""

👨‍🦱 --> scores 
------ make scores private by adding two underline at the beginning

👨‍🦱 -/-> __scores
👨‍🦱 --> controlled scores --> __scores
👨‍🦱 --> proxy property --> __scores

Proxy role:
    - access control level (ACL)  - authorization
    - validate - validation
    - ...

"""


std1 = Student(name="sabour", scores=[20, 20, 20, 20, 20, 20, 20, 19])

print(std1.grade())
# get
print(std1.scores)
# set
std1.scores = [20, 20, 20, 20, 20, 20, 20, 19]
# del
del std1.scores
print(std1.scores)
