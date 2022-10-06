class Car:
    def __init__(self, name, brand, is_wheel=True):
        self._name = name
        self._is_wheel = is_wheel
        self._brand = brand

    def moving_up(self):
        print(f"{self._name} is moving up")

    def moving_down(self):
        print(f"{self._name} is moving down")

    def moving_right(self):
        print(f"{self._name} is moving right")

    def moving_left(self):
        print(f"{self._name} is moving left")


class Saipa(Car):

    def __init__(self, name, model):
        brand = "saipa"
        self.__model = model
        super(Saipa, self).__init__(name=name, brand=brand)

    def show_brand(self):
        print("saipa brand")

    def capacity(self):
        print("limited")


class Irankhodro(Car):

    def __init__(self, name, model):
        brand = "Irankhodro"
        self.__model = model
        super(Irankhodro, self).__init__(name=name, brand=brand)

    def show_brand(self):
        print("Irankhodro brand")

    def capacity(self):
        print("unlimited")
