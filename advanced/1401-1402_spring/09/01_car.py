# @contents.setter    
# def contents(self, element):
#     self.__contents.append(element)

# @contents.deleter
# def contents(self):
#     self.__contents.clear()

# class AlakiObject:

#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self):
#         return self.__name

from time import sleep


class Car:

    def __init__(self, name):
        # private
        global my_street

        self.__name = name
        self.__pos = 0

        my_street.add_content(self.__pos, self)

    @property
    def name(self):
        return self.__name
    
    def move(self, direction):
        # check whether i can moev or not
            # update pos
            # update street content
        global my_street

        if direction == "forward":
            new_pos = self.__pos + 1

            if new_pos < my_street.length:
                my_street.remove_content(self.__pos, self)
                self.__pos = new_pos
                my_street.add_content(self.__pos, self)
        else:
            new_pos = self.__pos - 1

            if 0 <= new_pos:
                my_street.remove_content(self.__pos, self)
                self.__pos = new_pos
                my_street.add_content(self.__pos, self)


class Cell:
    def __init__(self, pos):
        self.__pos = pos
        self.__contents = []

    @property
    def pos(self):
        return self.__pos

    @property
    def contents(self):
        return self.__contents
    
    def add_content(self, element):
        # isinstance(element, int)
        # isinstance(element, Int)
        # isinstance(element, str)

        if isinstance(element, Car):
            self.__contents.append(element)
        else:
            print("Invalid elements")

    def remove_content(self, element):
        self.__contents.remove(element)

    def __str__(self):
        # " ".join(map(lambda x: x.name , self.__contents))
        # " ".join(map(lambda item: item.name , self.__contents))
        return " ".join(map(lambda item: item.name, self.__contents)).center(30)

    def __int__(self):
        return self.__pos

# cell1 = Cell(pos=0)
# alaki1 = AlakiObject(name="alaki1")
# alaki2 = AlakiObject(name="alaki2")
# cell1.add_content(alaki1)
# cell1.add_content(alaki2)

# cell1 -> cast to str -> invoke __str__
# print(cell1)
# str(cell1) == cell1.__str__

class Street:

    def __init__(self, name, length):
        self.__name = name
        self.__lenght = length
        self.__road = [Cell(pos=idx) for idx in range(self.__lenght)]

        # for idx in range(length):
        #     self.__road.append(Cell(pos=idx)) 
    
    @property
    def length(self):
        return self.__lenght

    def add_content(self, pos, element):
        # self.__road: [cell1, cell2, cell3, cell4]
        # Cell: self.__road[pos]
        # 
        self.__road[pos].add_content(element=element)

    def remove_content(self, pos, element):
        # self.__road: [cell1, cell2, cell3, cell4]
        # Cell: self.__road[pos]
        # 
        self.__road[pos].remove_content(element=element)

    def __str__(self):
        # self.__road: [cell1, cell2, cell3, cell4]
        # str(cell1) 
        # for cell in self.__road:
        #     ["peraido samando",  "peju", "porche"]
        #     "peraido samando | peju | porche"
        #     str(cell)
        return "|" + "|".join(map(str, self.__road)) + "|"


my_street = None

class GameEngine:

    def __init__(self):
        pass

    def run(self):
        global my_street

        rnd = 0
        my_street = Street(name="Shahid Bahounar", length=5)
        cars = [Car(name="peraido1"), Car(name="peraido2"), Car(name="peraido3")]

        while rnd < 10:
            car = cars[rnd % 3]
            car.move(direction="forward")
            sleep(0.9)
            print(my_street)
            rnd += 1


GameEngine().run()





