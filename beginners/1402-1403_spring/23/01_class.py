# class

"""
keyword
    - for
    - def
    - while
    - del
    - if
    - else
    - elif
    - global
    - nonlocal
    - return
    - yield
    - class
    - pass

built-in function:

keyword: class


naming convesion:
    - snake_case
    - PascalCase [x]
    - camelCase

class StudentStatus:
    pass
"""
# object
class Yoghurt:
    # constructor
    # __sth__
    # dunder method or magic function
    def __init__(self, ingredients, fat_rate, size): # params
        # self instance
        # current object
        # current instance
        
        # define property
        # self.[PROPERTY_NAME]
        # ingredients is the property of self
        # property              param
        self.ingredients = ingredients # property
        self.fat_rate = fat_rate
        self.size = size

    def delicious(self): # behaviour
        # self: current object
        print(f"{self.ingredients} am delicious, eat your heart out.")

    def sth(asghar):
        # asghar.ingredients
        pass

# instantiation
garlic_yoghurt = Yoghurt("garlic", "8-percentages", 2) # instance 1
onion_yoghurt = Yoghurt("onion", "2-percentages", 1) # instance 2
cucumber_yoghurt = Yoghurt("cucumber", "20-percentages", 3) # instance 3
eggplant_yoghurt = Yoghurt(size=3, ingredients="eggplant", fat_rate="20-percentages") # instance 4

# read property
# access property
# instance.property_name
print(garlic_yoghurt.ingredients)
print(garlic_yoghurt.fat_rate)
print(garlic_yoghurt.size)

print(onion_yoghurt.ingredients)


# access to the behaviour
# instance.behaviour()
garlic_yoghurt.delicious()
cucumber_yoghurt.delicious() # Yoghurt.delicious(cucumber_yoghurt)


# class Student:

    # constructor
