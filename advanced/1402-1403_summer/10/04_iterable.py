
class MyIterator:
    def __init__(self, iterable):
        self.__list = iterable
        self.__pointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            res = self.__list[self.__pointer]
        except IndexError:
            raise StopIteration from None
        else:
            self.__pointer += 2
            return res


class MyIterable:

    def __init__(self, iterable):
        self.__list = iterable

    def __iter__(self):
        return MyIterator(self.__list)


my_list = [1, 2, 3, 4, 5, 6, 7]
my_iterable = MyIterable(my_list)
my_iterator = iter(my_iterable)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
