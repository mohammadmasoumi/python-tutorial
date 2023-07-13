
from abc import ABC, abstractmethod


class AbstractEmployee(ABC):

    def __init__(self, name):
        super().__init__()

    @abstractmethod
    def get_salary(self):
        pass


class Employee(AbstractEmployee):

    def __init__(self, name):
        self.name = name
        super().__init__(name)


class FullyEmployee(Employee):

    def __init__(self, name, salary):
        self.salary = salary
        super().__init__(name)

    def get_salary(self):
        return self.salary


class HourlyEmployee(Employee):

    def __init__(self, name, work_hour, wage):
        self.work_hour = work_hour
        self.wage = wage
        super().__init__(name)

    def get_salary(self):
        return self.work_hour * self.wage
