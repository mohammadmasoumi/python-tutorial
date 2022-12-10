class Point:

    def __init__(self,x,y):

        self.x = x
        self.y = y
    def __add__(self,obj):
        if isinstance(obj, Point):
            return Point(self.x + obj.x, self.y + obj.y)
        else:
            pass
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __mul__(self,obj):
        if isinstance(obj, Point):
            return Point(self.x * obj.x, self.y * obj.y)
        elif isinstance(obj, int):
            return Point(self.x * obj, self.y * obj)
        else:
            raise ValueError(f"Unsupported {type(self)} + {type(obj)}") 


    def __sub__(self,obj):
        if isinstance(obj, Point):
            return Point(self.x - obj.x, self.y - obj.y)
        else:
            pass    

    def __floordiv__(self,obj):
        if isinstance(obj, Point):
            return Point(self.x / obj.x, self.y / obj.y)
        elif isinstance(obj, int):
            return Point(self.x / obj, self.y / obj)
        else:
            raise ValueError(f"Unsupported {type(self)} + {type(obj)}")

    def __truediv__(self,obj):
        if isinstance(obj, Point):
            return Point(self.x // obj.x, self.y // obj.y)
        elif isinstance(obj, int):
            return Point(self.x // obj, self.y // obj)
        else:
            raise ValueError(f"Unsupported {type(self)} + {type(obj)}")
    def __eq__(self,obj):
        if isinstance(obj, Point):
            return True if self.x == obj.x and self.y == obj.y else False
        else:
            pass
        
    def __ne__(self,obj):
        if isinstance(obj, Point):
            return False if self.x == obj.x and self.y == obj.y else True
        else:
            pass

    def __gt__(self,obj):
        if isinstance(obj, Point):
            return True if self.x > obj.x and self.y > obj.y else False
        else:
            pass

    def __ge__(self,obj):
        if isinstance(obj, Point):
            return True if self.x >= obj.x and self.y >= obj.y else False
        else:
            pass

    def __lt__(self,obj):
        if isinstance(obj, Point):
            return True if self.x < obj.x and self.y < obj.y else False
        else:
            pass

    def __le__(self,obj):
        if isinstance(obj, Point):
            return True if self.x < obj.x and self.y < obj.y else False
        else:
            pass            

point1 = Point(20, 20)
point2 = Point(5, 12)



print(point1*point2)
print(point1*3)
print(point1-point2)
print(point1/point2)
print(point1/2)
print(point1//point2)
print(point1//4)
print(point1==point2)
print(point1!=point2)
print(point1>point2)
print(point1>=point2)