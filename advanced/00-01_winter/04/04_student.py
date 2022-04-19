# attribute

class Student:
    # constructor

    # national_id, personality_type, father_name, pet_name, height
    def __init__(self, name, age):
        # instanc: self
        #    attr   value
        # attribute
        self.name = name
        self.n = name
        self.age = age

    # behaviour
    def move(self):
        print(f"[{self.name}]: I am moving")


std1 = Student(name="Asghar", age=12)
print(std1.name)
print(std1.n)
print(std1.age)
std1.move()

std2 = Student(name="Akbar", age=14)
print(std2.name)
print(std2.n)
print(std2.age)
std2.move()

# name: asghar
# national_id: 1002
# personality_type: ISTJ
# father_name: asghar
# pet_name: malmal
# height: 198

# name: akbar
# national_id: 1002
# personality_type: ISTJ
# father_name: akbar
# pet_name: malmal
# height: 198
