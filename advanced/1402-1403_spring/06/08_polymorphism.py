# polymorphism with class method

class Tomato:
    
    def typ(self):
        return "Vegetable"

    def color(self):
        return "Red"

class Apple:

    def typ(self):
        return "Fruit"

    def color(self):
        return "Green"


my_list = [Apple(), Tomato()]

for item in my_list:
    print(item.typ())
    print(item.color())
