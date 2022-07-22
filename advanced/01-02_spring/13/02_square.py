
class Rectangle:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def s(self):
        return self.x * self.y        

    @property
    def p(self):
        return 2 * (self.x + self.y)        


class Square(Rectangle):
    
    def __init__(self, x):
        super().__init__(x=x, y=x)



s1 = Square(10)
print(s1.p)
print(s1.s)
