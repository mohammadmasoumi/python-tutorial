# IS A

"""
IS A
    student is a human.
    tomato is a vegetable.
    apple is a fruit.

    ---------
    | HUMAN |
    ---------
        ^
        |
    -----------
    | STUDENT |
    -----------


    BASE CLASS
    -------------
    | Vegetable |
    -------------
        ^
        |
    -----------
    |  Tomato |
    -----------
    DRIVED CLASS
    مشتق شده

"""

class Human:
    pass


class Student(Human):
    pass


class Vegetable:
    pass


class Tomato(Vegetable):
    pass
