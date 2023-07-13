# Object Oriented programming
# Object

# Student
# Class
# Car
# Bus
# Human

# essentical factors of object
# - properties
# - behaviour


# Student
# - properties: [variable][usefull in problem space]
#   - name
#   - knowledge
#   - age
#   - height
#   - weight
#   - grade
#   - ...
# - behaviours: [function]
#   - study -> effect on properties - increase knowledge
#   - walk
#   - run
#   - speak
#   - sleep
#   - ...

# keyword: class
# reserved keyword
# def, for, while, return, ...

# notation: PascalCase, PascalCasing
# StudentNumber
# BattleShip

"""
windows + dot -> emoji

            Student
        -------------
name -> |    👶     |
height->|           | --->  👱‍♂️👱‍♀️👩‍🦲👨‍🦲 instance
        -------------

        👱‍♂️ 
        name: Ali
        height: 145
        base: 7th
        ... 

        👱‍♀️
        name: Sara
        height: 160
        base: 7th
        ...

"""
# built-in function
# print
# sum
# input


class Student:

    # __sth__
    # magic function or dunder method

    # params VS argument
    # params: function paramethers
    # argument: value of params

    # Constructor
    # student_height=170
    # default value for a param
    def __init__(self, student_name, student_height=170):
        # self: 👶
        # 👶.name = "asghar"
        # 👶.height = 180
        # current object/instance: self
        # attach property
        self.name = student_name
        self.height = student_height


# TypeError: Student.__init__() got multiple values for argument 'self'
# student1 = Student(self="1", student_name="asghar")
student1 = Student(student_name="asghar")  # instance 1 👱‍♂️
student2 = Student(student_name="ahmad")  # instance 2 👨‍🦲

# access
print(student1.name)
print(student2.name)
