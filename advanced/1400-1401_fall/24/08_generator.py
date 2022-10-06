class MyGenerator:

    def __init__(self, max):
        self._num = -1
        self._max = max

    def __iter__(self):
        return self

    def __next__(self):
        self._num += 1

        if self._num == self._max:
            raise StopIteration

        return self._num ** 2


gen = MyGenerator(10)
for item in gen:
    print(item)
