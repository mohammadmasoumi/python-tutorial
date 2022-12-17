
class Student:

    # 1. attribute or property
    # 2. behaviour

    def __init__(self, name):
        self.name = name
        # 1. private
        self.__grade = 19

    # get
    @property
    def secratory(self):
        return self.__grade 

    # set
    @secratory.setter
    def secratory(self, value):
        #  validation
        if 0 <= value <= 20:
            self.__grade = value 
    
    # del
    @secratory.deleter
    def secratory(self):
        self.__grade = 0


# Client -> grade -> __grade

# attr action
# 1. get
# 2. set
# 3. del

std1 = Student("mina")
print(std1.name)
print(std1.secratory) # get
std1.secratory = 22 # set
std1.secratory = 10 # set
print(std1.secratory)
del std1.secratory # del
print(std1.secratory)

# AttributeError: 'Student' object has no attribute '__grade'
# print(std1.__grade) # get
# std1.__grade = -1 # set
# del std1.__grade # del
