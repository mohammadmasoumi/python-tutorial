
class MyList:

    def __init__(self):
        self.__pos = 0
        self.__list = []

    def append(self, item):
        self.__list.append(item)

    def extend(self, items):
        self.__list.extend(items)

    def update(self, index, item):
        self.__list[index] = item

    def __iter__(self): # iterable
        # return iter(self.__list)
        # return self
        new_iterator = MyList()
        new_iterator.extend(self.__list)

        return new_iterator 

    def __next__(self): # iterator
        try:
            res = self.__list[self.__pos]
            self.__pos += 1
            return res
        except IndexError:
            raise StopIteration from None

my_list = MyList() # IterableX Iterator
my_list.extend([1, 2, 3, 4, 5])

# iter(object)
# object.__iter__()
# iterator = iter(self.__list)
# next(iterator)
# iterator.__next__()
# my_list = iter(my_list)
# next(my_list)
# my_list.__next__()
# next()

# iterator = iter(my_list)
# print(next(iterator))

print(next(my_list))
print(next(my_list))
print(next(my_list))

# my_list = my_list.__iter__()
# iterator = my_list
iterator = iter(my_list) 
print(next(iterator))
print(next(iterator))
# print(next(iterator))