from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self, m):
        pass


class FulltimeEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_salary(self):
        print(self.salary)

class ParttimeEmployee(Employee):
    
    def __init__(self, name, workhour, rate):
        super().__init__(name)
        self.workhour = workhour
        self.rate = rate

    def get_salary(self):
        print(self.workhour * self.rate * 12)


e1 = FulltimeEmployee("e1", 120000)
e1.get_salary()

e2 = ParttimeEmployee("e2", 6, 60000)
e2.get_salary()

