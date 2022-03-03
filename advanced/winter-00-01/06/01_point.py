# dunder method 
# magic function
# __method_name__

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # other = point2
        #print(f"x: {self.x}, y: {self.y}")
        #print(f"other x: {other.x} , other y: {other.y}")
        

        return Point(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        # زمانی که آبجکت را به استرینگ کست میکنیم این تابع فراخوانی میشود
        return f"x: {self.x}, y: {self.y}"


point1 = Point(10, 10)
point2 = Point(20, 20)

# print(str(point1))
# print(point1) # x: 10, y: 10
# print(point1.x)
# print(point1.y)

# Point(point1.x + point2.x , point1.y + point2.y)
# point1.+(point2)
print(point1 + point2)
print(point1 + 12)
print(point2 + point1)