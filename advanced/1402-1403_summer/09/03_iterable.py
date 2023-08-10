
"""
-7 -6 -5 -4 -3 -2 -1 
0  1  2  3  4  5  6
1  2  3  4  5  6  7

1. 
start < 0 -1
end < 0 -4
step < 0 -2 

pos > end

2. 
start < 0
end < 0
step > 0

pos < end

3. 
...


"""


class MyIter:

    def __init__(self, iterable, start, end, step):
        self.__iterable = iterable
        self.__pos = start
        self.__end = end
        self.__step = step

        if self.__step == 0:
            raise ValueError("step can't be zero!")

    def __iter__(self):
        return self

    def __next__(self):
        if self.__pos >= self.__end:
            raise StopIteration 
        try:
            item = self.__iterable[self.__pos]
        except IndexError:
            raise StopIteration from None
        else:
            self.__pos += self.__step

        return item

#          0  1  2  3  4  5  6
my_list = [1, 2, 3, 4, 5, 6, 7]
iterator = MyIter(iterable=my_list, start=1, end=4, step=2)


for item in iterator:
    print(item)