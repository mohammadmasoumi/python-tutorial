# TypeError: 'list' object is not an iterator
my_test = [1, 2, 3]
# print(next(my_test))

class MyIterable:

    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        return iter(self.sequence)
    

my_iterable = MyIterable(my_test)
# TypeError: 'MyIterable' object is not an iterator
print(next(my_iterable))