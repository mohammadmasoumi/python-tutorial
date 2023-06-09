import time
import keyboard

# CAR_2_STYLE = {
#     'taxi': '🚕',
#     'police': '🚓',
#     'personal': '🚗'
# }
CAR_2_STYLE = {
    'taxi': 'T',
    'police': 'P',
    'personal': 'O'
}
# constant
CELL_WIDTH = 11


class Car:

    def __init__(self, x, y, plate, typ, passenger):
        # car position in street
        self.x = x
        self.y = y

        self.plate = plate

        if typ not in CAR_2_STYLE.keys():
            raise ValueError(
                f'invalid typ, valid types are: {CAR_2_STYLE.keys()}')

        self.typ = typ
        self.passenger = passenger

        # add car in street
        global street
        street.add_content(self.x, self.y, self)

    def move_right(self):
        global street

        new_x = self.x + 1
        if 0 <= new_x < street.length:
            street.remove_content(self.x, self.y, self)
            self.x = new_x
            street.add_content(self.x, self.y, self)

    def move_left(self):
        global street

        new_x = self.x - 1
        if 0 <= new_x < street.length:
            street.remove_content(self.x, self.y, self)
            self.x = new_x
            street.add_content(self.x, self.y, self)

    def move_top(self):
        global street

        new_y = self.y - 1
        if 0 <= new_y < street.width:
            street.remove_content(self.x, self.y, self)
            self.y = new_y
            street.add_content(self.x, self.y, self)

    def move_bottom(self):
        global street

        new_y = self.y + 1
        if 0 <= new_y < street.width:
            street.remove_content(self.x, self.y, self)
            self.y = new_y
            street.add_content(self.x, self.y, self)

    def move(self, direction):
        if direction == 'right':
            self.move_right()
        elif direction == 'left':
            self.move_left()
        elif direction == 'top':
            self.move_top()
        elif direction == 'bottom':
            self.move_bottom()

    def __int__(self):
        return int(self.plate)

    def __str__(self):
        # if self.typ == 'taxi':
        #     return '🚕'
        # elif self.typ == 'police':
        #     return '🚓'
        # else:
        #     return '🚗'
        return CAR_2_STYLE.get(self.typ)

# ValueError: invalid typ, valid types are: ['taxi', 'police', 'personal']
# taxi = Car('021', 'taxi2', 10)

# taxi = Car('021', 'taxi', 3)
# # str(taxi) taxi.__str__
# # implicit casting to string
# print(taxi)  # print(str(taxi))
# # print(int(taxi))  # taxi.__int__


class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contents = []

    def add_content(self, element):
        self.contents.append(element)

    def remove_content(self, element):
        self.contents.remove(element)

    def __str__(self):
        return "-".join([str(content) for content in self.contents])


class Lane:

    def __init__(self, number, length):
        self.number = number
        self.length = length

        self.lane = [Cell(x=x, y=self.number) for x in range(self.length)]

    def add_content(self, x, element):
        cell = self.lane[x]
        cell.add_content(element)

    def remove_content(self, x, element):
        cell = self.lane[x]
        cell.remove_content(element)

    def __str__(self):
        return "|" + "|".join([str(cell).center(CELL_WIDTH) for cell in self.lane]) + "|"


class Street:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.street = [Lane(number=y, length=self.length)
                       for y in range(self.width)]
        """
        -----------------------
        - - - - - - - - - - - - Lane(number=0, length=13)
        -----------------------
        - - - - - - - - - - - - Lane(number=1, length=13)
        -----------------------
        - - - - - - - - - - - - Lane(number=2, length=13)
        -----------------------
        """

    def add_content(self, x, y, element):
        lane = self.street[y]
        lane.add_content(x, element)

    def remove_content(self, x, y, element):
        lane = self.street[y]
        lane.remove_content(x, element)

    def __str__(self):
        """
        -------------\n|           |           |           |\n-------------\n
        """
        line = "-" * ((self.length * (CELL_WIDTH + 1)) + 1)
        scratch = "".join(
            [line + "\n" + str(lane) + "\n" for lane in self.street])
        scratch += line + "\n"
        return scratch


street = Street(length=10, width=3)
# print(street)

taxi = Car(0, 0, '021', 'taxi', 3)
# print(taxi)
print(street)

KEY_2_DIRECTION = {
    'w': 'top',
    'a': 'left',
    's': 'bottom',
    'd': 'right',
}

while True:
    # time.sleep(0.5)
    # direction = input()
    action_key = keyboard.read_key()

    if keyboard.is_pressed(action_key):
        if action_key in KEY_2_DIRECTION.keys():
            taxi.move(KEY_2_DIRECTION.get(action_key))
            print(street)


# DIRECTION_2_MOVE = {
#     'right': lambda: self._move(self.x+1, self.y),
#     'left': lambda: self._move(self.x-1, self.y),
#     'top': lambda: self._move(self.x, self.y-1),
#     'bottom': lambda: self._move(self.x, self.y+1),
# }
# move_function = DIRECTION_2_MOVE.get(direction)
# move_function()