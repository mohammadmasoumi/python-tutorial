
class MyIter:

    def __init__(self, iterable, skip):
        self.__iterable = iterable
        self.__skip = skip
        self.__pos = 0

    # iter(instance)
    # [BE CAREFUL]: used in for loop 
    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__iterable[self.__pos]
        except IndexError:
            raise StopIteration from None
        else:
            self.__pos += self.__skip
        
        return item

my_list = [1, 2, 3, 4, 5, 6, 7]
# iter(my_list)
iterator = MyIter(iterable=my_list, skip=3)

print(next(iterator))
print(next(iterator))

# iter(iterator)
for item in iterator:
    print(item)