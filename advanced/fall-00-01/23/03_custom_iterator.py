# iter()
my_list = [1, 2, 3, 4, 5]


class CustomIterator:
    # data[index]
    def __init__(self, data):
        self._index = -1
        self._data = data

    def __iter__(self):
        # برای استفاده از iter

        # return self
        # return iter([1, 2, 3])
        # return None
        return self

    def __next__(self):
        try:
            self._index += 1
            return self._data[self._index]

        except IndexError:
            raise StopIteration


custom_iterator = CustomIterator(my_list)
# custom_iterator = iter(custom_iterator)

for item in custom_iterator:
    print(item)
