
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_greeting1(self):
        print("hello")

    @staticmethod
    def say_greeting2():
        print("hello")

    @staticmethod
    def say_hello(name):
        print(f"Hello {name}")
        Person.say_greeting2()


# factory method
person1 = Person("asghar", 22)
Person.say_hello("Asghar")
person1.say_hello("Akbar")
person1.say_greeting1()


type("A", (), {})