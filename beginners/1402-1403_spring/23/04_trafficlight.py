
class Car:
    def __init__(self, pos, plate, headseatters):
        self.pos = pos
        self.plate = plate
        self.headseatters = headseatters

        global street
        street.add_content(self)

    def move_right(self):
        street.move_content(self, self.pos + 1)

    def move_left(self):
        street.move_content(self, self.pos - 1)

    def __str__(self):
        return "🚗"

class Bus:
    def __init__(self, pos, plate, headseatters):
        self.pos = pos
        self.plate = plate
        self.headseatters = headseatters

        global street
        street.add_content(self)

    def move_right(self):
        street.move_content(self, self.pos + 1)

    def move_left(self):
        street.move_content(self, self.pos - 1)

    def __str__(self):
        return "🚎"

class Street:
    def __init__(self, length):
        self.length = length
        self.contents = [[] for _ in range(self.length)]
    
    def add_content(self, element):
        if 0 <= element.pos < self.length:
            self.contents[element.pos].append(element)

    def move_content(self, element, new_pos):
        if 0 <= new_pos < self.length:
            self.contents[element.pos].remove(element)
            element.pos = new_pos
            self.contents[element.pos].append(element)

    def __str__(self):
        return "|" + "|".join(["-".join([str(c) for c in content]).center(11) for content in self.contents]) + "|"

            
                

street = Street(10)
# print(str(street))

car1 = Car(pos=0, plate="007", headseatters=2)
# print(street)
bus1 = Bus(pos=1, plate="021", headseatters=20)
# print(street)
car1.move_left()
# print(street)
print(street)

import time
while True:
    time.sleep(1)
    car1.move_right()
    print(street)