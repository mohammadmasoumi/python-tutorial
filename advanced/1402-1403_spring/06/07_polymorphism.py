# polymorphism with function and object

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


def func(obj):
    print(obj.typ())
    print(obj.color())


tomato = Tomato()
apple = Apple()

func(tomato)
func(apple)