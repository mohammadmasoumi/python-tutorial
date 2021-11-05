class Parrot:
    # """Parrot"""
    # raw input
    """
    Parrot
    ----------
    ----------
    """
    # class property
    # constant for all instances
    species = "Bird"

    # instance property
    def __init__(self, name, age):
        """

        :param name:
        :param age:
        """

        # during development
        assert isinstance(age, int), f"`age` should be int, but got {type(age)}"

        # user error
        if not isinstance(age, int):
            # age = int(age)
            raise ValueError(f"`age` should be int, but got {type(age)}")

        self._name = name
        self._age = age

    # just change the instance properties
    @property
    def home_address(self):
        return f"{self._name} lives in jungle."

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age

    def set_name(self, name):
        """

        :param name:
        :return:
        """
        self._name = name

    def get_name(self):
        """

        :return:
        """
        return self._name

    def del_name(self):
        """

        :return:
        """
        del self._name

    # behavior
    def fly(self):
        print(f"{self._name} is flying")


blue = Parrot("blue", 19)
red = Parrot("red", 19)

print(f"blue.species: {blue.species}")
print(f"red.species: {red.species}")
# blue.age = 22
# print(blue.age)
# del blue.age
print(f"My parrot name is: {blue.get_name()}")
blue.set_name("purple")
print(f"My parrot name is: {blue.get_name()}")
# blue.del_name()
# print(f"My parrot name is: {blue.get_name()}")

print(f"My Parrot is {blue.age} years old.")
blue.age = 22
print(f"My Parrot is {blue.age} years old.")

print(blue.home_address)
# print(blue.home_address())

# del blue.age
# AttributeError: 'Parrot' object has no attribute '_age'
# print(f"My Parrot is {blue.age} years old.")


# dunder or magic method
with open("doc.txt", "w") as file:
    file.write(blue.__doc__)

# print(blue.__doc__)
# print(blue.__doc__)
# print("""
# Hello from the other side
# print
# print
# print
# print
# """)
# print('''
# Hello from the other side
# print
# print
# print
# print
# ''')
