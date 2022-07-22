# builtin function
# iter()


class MyIterator:

    def __init__(self, iterable, offset):
        self.iterable = iterable
        self.index = -1
        self.offset = offset

    def __iter__(self):
        return self

    def __next__(self):
        self.index += self.offset

        try:
            return self.iterable[self.index]
        except IndexError:
            raise StopIteration()


my_iter = MyIterator([1, 2, 3 ,4], 3)

for item in my_iter:
    print(item)


print("-------------------------")
for item in my_iter:
    print(item)