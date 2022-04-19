# OOP
# behaviour
# attribute

a = 12
b = 13

# class name is Pascal: StudentService
class Student:

    # behaviour
    def move(self):
        print("I am moving")

    def move_with_input(self, name):
        print(f"[{name}]: I am moving")


#      Student()
# std1 variable
# asghar = Student() 
std1 = Student()
std2 = Student()

# a, b are variables
a = Student()
b = Student()

# call, invoke behaviour
# instance_name.behaviour()
std1.move()
std1.move_with_input("Ali")
std2.move()
std2.move_with_input("Hassan")

# list_students
students_list = []
for idx in range(100):
    std = Student() 
    #students_list.append(std)
    students_list.append(Student())

print(students_list)