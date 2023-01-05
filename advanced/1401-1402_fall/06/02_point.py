class Point:

    def __init__(self, x: int, y: int) -> None:
        # self:
        # x, y
        self.x = x + 10
        self.y = y

    def __eq__(self, asghar):

        if isinstance(asghar, int):
            raise ValueError("Raised sth")

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(20, 20)
p2 = Point(10, 10)

print(p1, p2)
