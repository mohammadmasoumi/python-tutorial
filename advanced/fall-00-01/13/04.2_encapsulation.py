class Computer:

    def __init__(self):
        self.__max_price = 900

    def change_price(self, price):
        if price > self.__max_price:
            self.__max_price = price

    def show_price(self):
        print(f"current price is: {self.__max_price}")

    def sell(self):
        print(f"computer has been sold in {self.__max_price}")


# copyright()
computer = Computer()
computer.change_price(800)
computer.show_price()
computer.change_price(1000)
computer.show_price()
computer.sell()
