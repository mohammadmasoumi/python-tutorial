# encapsulation 

class Computer:
    # با اینکار کسی از بیرون نمیتواند ویژگی های کلاس رو دستکاری کند.
    def __init__(self) -> None:
        # private property
        self.__max_price = 900

    def set_max_price(self, new_max_price):
        if new_max_price > self.__max_price:
            self.__max_price = new_max_price

    def sell(self):
        print(f"Selling computer at {self.__max_price}")

    
computer1 = Computer()
computer1.__max_price = 10
computer1.set_max_price(1000)
computer1.sell()