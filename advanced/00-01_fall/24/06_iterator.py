my_iter = iter([1, 2, 3, 4])

for item in my_iter:
    print(f"item1: {item}")

for item in my_iter:
    print(f"item2: {item}")


class MyIterator:

    def __init__(self, data):
        self._data = data
        self._index = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self._index += 1
            return self._data[self._index]
        except IndexError:
            raise StopIteration


# iter()  <=> MyIterator
# iter(my_list) MyIterator(my_list)

my_list = [1, 2, 3, 4, 5, 6]
iterator = MyIterator(my_list)

print(next(iterator), iterator._index)
print(next(iterator), iterator._index)
print(next(iterator), iterator._index)
print(next(iterator), iterator._index)
print(next(iterator), iterator._index)
print(next(iterator), iterator._index)

for item in iterator:
    print(item)

for item in iterator:
    print(item)
