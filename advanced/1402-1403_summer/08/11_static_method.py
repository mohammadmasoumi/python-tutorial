
class ShahidSattariStudent:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def get_school():
        # self
        # no need for properties and behaviours
        # properties: self.name
        # behaviours: self.get_name()
        return "ShahidSattari"

sabour = ShahidSattariStudent("sabour", 15)
print(sabour.get_school())