"""
MyIterator
    __iter__
    __next__
        += 2

MyIterable
    __iter__
        return MyIterator(self.__list)             

next(iter(my_iterable))

"""
class MyIterator:

    def __init__(self, iterable):
        self.__list = iterable
        self.__pointer = 0

    def __iter__(self): 
        # iterator: self
        # next(iterator)
        # next(iterator)

        # __next__
        # return iter(self.__list)

        # iterator ->
        #   __iter__
        #   __next__

        # iterable ->
        #   __iter__
        # iter(self.__list)

        # Only define next
        #   __next__
        # problem ??
        # for

        # iter(self.__list) -> __next__ X
        # return iter(self.__list)

        return self

    def __next__(self):
        try:
            res = self.__list[self.__pointer]
        except IndexError:
            raise StopIteration from None
        else:
            self.__pointer += 1
            return res


my_list = [1, 2, 3, 4]
my_iterable = MyIterator(my_list)
my_iterator = iter(my_iterable) # my_iterable.__iter__() 
print(id(my_iterable), id(my_iterator))
# iterator = iter(my_list) # my_list.__iter__()

# TypeError: 'MyIterator' object is not iterable
# iter(item) -> item.__iter__()
# iterator: iter(my_iterator)
# next(iterator)
# for item in my_iterator:
#     print(item)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
