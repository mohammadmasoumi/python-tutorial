class Tyre:
    def __init__(self, brand):
        self._brand = brand

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @brand.deleter
    def brand(self):
        del self._brand

    def __str__(self):
        return f"tyre: {self._brand}"


class Gear:
    def __init__(self, gear_count: int = 5, automated: bool = False):
        self._gear_count = gear_count
        self._automated = automated

    @property
    def gear_count(self):
        return self._gear_count

    @property
    def automated(self):
        return self._automated

    def __str__(self):
        str_automated = 'automated' if self._automated else ''
        return f"gear: {self._gear_count} {str_automated}"


class Tormoz:
    def __init__(self, is_abs: bool = False):
        self._is_abs = is_abs

    @property
    def is_abs(self):
        return self._is_abs

    def __str__(self):
        str_is_abs = 'is abs' if self.is_abs else ''
        return f"tormoz: {str_is_abs}"


class Car:

    def __init__(self, name, tyre, gear, tormoz):
        # concrete
        self._name = name
        self._tyre = tyre
        self._gear = gear
        self._tormoz = tormoz

    def show(self):
        print(f"{self._name}: {self._tormoz}, {self._gear}, {self._tyre}")


# tyres
alborz_tyre = Tyre("Alborz")
asghar_tyre = Tyre("Asghar")

# gears
gear6 = Gear(6)
automated_gear7 = Gear(6, True)

# tormoz
tormoz_abs = Tormoz(True)
tormoz_adi = Tormoz()

# instantiating cars
peraido = Car(name="Peraido 161", tyre=alborz_tyre, gear=automated_gear7, tormoz=tormoz_abs)
peraido.show()

# name = "mohammad"
# # name = "ali"
# s = f"salam: {name}"
# s = "salam mohammad"
