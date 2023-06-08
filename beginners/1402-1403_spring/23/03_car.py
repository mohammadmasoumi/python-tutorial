
class Car:

    def __init__(self, driver ,hp):
        self.driver = driver
        self.hp = hp

    def crash(self, car): # car: car2
        # self: car1
        # car: car2
        self.hp -= 80
        car.hp -= 80  



car1 = Car("asghar", 80)
car2 = Car("soghra", 100)
car1.crash(car2)

print(car1.hp)
print(car2.hp)