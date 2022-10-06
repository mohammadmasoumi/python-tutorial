
class MyIterator:
    def __init__(self, my_list) -> None:
        self.my_list = my_list
        self.pointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item =  self.my_list[self.pointer]
        except IndexError:
            raise StopIteration()
        else:
            self.pointer += 1
            return item

my_iter = MyIterator([1, 2, 3, 4])
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


my_iter2 = iter([1, 2, 3, 4])