knowledge = -100

class Student:
    def __init__(self, name, age):
        self.fname = name
        self.lname = "asghari"
        self.age = age + 1
        self.knowledge = -100

    def study(self): # self: soghra, asghar
        global knowledge
        knowledge -= 100 
        self.knowledge = knowledge


asghar = Student(name="asghar",age=2)
akbar = Student(name="akbar",age=22)
soghra = Student(name="kobra",age=222)

asghar.study()
akbar.study()

print(f"asghar.knowledge: {asghar.knowledge}")
print(f"akbar.knowledge: {akbar.knowledge}")

