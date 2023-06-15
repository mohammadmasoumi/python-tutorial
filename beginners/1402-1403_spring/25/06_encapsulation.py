class Student:
    def __init__(self, name, scores):
        self.name = name
        self.__scores = scores  # private
        # _ convension
        # _property_name -> private
        # accessable
        # _ or __

    # access - read
    @property
    def scores(self):
        return self.__scores

    # update
    @scores.setter
    def scores(self, new_value):
        # return
        if isinstance(new_value, list):
            for score in new_value:
                if score > 20 or score < 0:
                    break
            else:
                self.__scores = new_value
        # else:
        #     self.__scores = [20, 20, 20, 20]

    # del, set, get descriptor
    @scores.deleter
    def scores(self):
        self.__scores.clear()

    @property
    def grade(self):
        return sum(self.__scores) // len(self.__scores)


mahdi = Student("mahdi", [10, 10, 10, 10, 10])

# private
# set, get, del

print(mahdi.grade)
print(mahdi.scores)
# mahdi.scores = [20, 22, 10]
mahdi.scores = [20, 20, 20]
print(mahdi.scores)
del mahdi.scores
print(mahdi.scores)


# print(mahdi.name)  # access
# mahdi.name = "asghar"  # update
# del mahdi.name  # delete
