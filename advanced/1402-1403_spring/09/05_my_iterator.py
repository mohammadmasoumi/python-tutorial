
class MyIter:

    def __init__(self, iterable, skip):
        self.iterable = iterable
        self.skip = skip
        self.pointer = 0

    def __iter__(self): # iter(my_iter)
        return self
    
    def __next__(self):
        if self.pointer < len(self.iterable):
            item =  self.iterable[self.pointer]
            self.pointer += self.skip
            return item
        else:
            # raise StopIteration()
            self.pointer = 0
            item = self.iterable[self.pointer]
            self.pointer += self.skip
            return item
        
my_list = [1, 2, 3, 4]
my_iter = MyIter(my_list, 3)
# print(next(my_iter))
# print(next(my_iter))
# # print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

import time
for item in my_iter:
    time.sleep(0.5)
    print(item)


