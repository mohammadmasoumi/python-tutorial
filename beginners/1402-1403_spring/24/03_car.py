import keyboard

CAR_2_STYLE = {'taxi': 'T', 'police': 'P', 'personal': 'O'}
CELL_WIDTH = 11


class Car:

    def __init__(self, x, y, plate, typ, passenger):
        self.x, self.y = x, y
        self.plate = plate
        self.typ = typ
        self.passenger = passenger
        if typ not in CAR_2_STYLE.keys():
            raise ValueError(
                f'invalid typ, valid types are: {CAR_2_STYLE.keys()}')
        global street
        street.add_content(self.x, self.y, self)

    def _move(self, new_x, new_y):
        if 0 <= new_x < street.length and 0 <= new_y < street.width:
            street.remove_content(self.x, self.y, self)
            self.x, self.y = new_x, new_y
            street.add_content(self.x, self.y, self)

    def move(self, direction):
        {
            'right': lambda: self._move(self.x+1, self.y),
            'left': lambda: self._move(self.x-1, self.y),
            'top': lambda: self._move(self.x, self.y-1),
            'bottom': lambda: self._move(self.x, self.y+1),
        }.get(direction)()

    def __int__(self):
        return int(self.plate)

    def __str__(self):
        return CAR_2_STYLE.get(self.typ)


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

    def add_content(self, x, y, element):
        lane = self.street[y]
        lane.add_content(x, element)

    def remove_content(self, x, y, element):
        lane = self.street[y]
        lane.remove_content(x, element)

    def __str__(self):
        line = "-" * ((self.length * (CELL_WIDTH + 1)) + 1)
        scratch = "".join(
            [line + "\n" + str(lane) + "\n" for lane in self.street])
        scratch += line + "\n"
        return scratch


street = Street(length=10, width=3)
taxi = Car(0, 0, '021', 'taxi', 3)
KEY_2_DIRECTION = {'w': 'top', 'a': 'left', 's': 'bottom', 'd': 'right', }

while True:
    action_key = keyboard.read_key()
    if keyboard.is_pressed(action_key):
        if action_key in KEY_2_DIRECTION.keys():
            taxi.move(KEY_2_DIRECTION.get(action_key))
            print(street)
