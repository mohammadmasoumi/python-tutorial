class CustomGenerator:

    def __init__(self, stop):
        self._item = 0
        self._stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self._item > self._stop:
            raise StopIteration

        # pow(2, 10)
        # 2 ** 10
        # yield self._item * self._item
        self._item += 1
        # return self._item ** 2
        return 2 ** self._item


gen = CustomGenerator(10)
for item in gen:
    print(item)
