# encapsulation
# vscode shortcut in windows

class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name[0].upper() == new_name[0]:
            self.__name = new_name

    # def change_name(self, new_name):
    #     # new_name: aliasghar
    #     # new_name[0]: a
    #     # new_name[0].upper(): A
    #     # new_name[0].upper() == new_name[0]
    #     if not isinstance(new_name, str):
    #         raise TypeError(f"new_name must be str, got {type(new_name)}")

    #     if new_name[0].upper() == new_name[0]:
    #         self.__name = new_name
    #     else:
    #         raise ValueError("new_name is not valid. new_name must start with capitalcase.")        

    def __str__(self):
        return f"name: {self.__name}, age: {self.__age}"


person1 = Person("aliakbar", 17)
# person2 = Person("ali", 21)

# how to change person1's name?
# you can not even access to the __name property
# AttributeError: 'Person' object has no attribute '__name'
# person1.__name = "aliasghar"
# print(person1.__name)

# print(person1)
# person1.change_name(12)
# person1.change_name("aliasghar")
# person1.change_name(input())
print(person1)
print(person1.get_name())
print(person1.name)

#property_name.setter
person1.name = "Aliasghar"
print(person1.name)

# # define a new function - encasulated [tick]
# person1.change_name("aliakbar")
# print(person1.name)
