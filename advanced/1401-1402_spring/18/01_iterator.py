
class MyIterator:
    def __init__(self, start, end, step) -> None:
        self.start = start
        self.end = end
        self.step = step
        self.curr = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr > self.end:
            raise StopIteration()

        prev_curr = self.curr
        self.curr += self.step
        return prev_curr

my_iter = MyIterator(0, 10, 2)

print(next(my_iter))