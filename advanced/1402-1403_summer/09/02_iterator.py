
class MyIter:

    def __init__(self, iterable, start, end, step):
        if step == 0:
            raise ValueError("step can't be zero!")

        self.__iterable = iterable
        self.__pos = start
        self.__end = end
        self.__step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.__pos > self.__end:
            raise StopIteration

        try:
            item = self.__iterable[self.__pos]
        except IndexError:
            raise StopIteration
        else:
            self.__pos += self.__step

        return item
