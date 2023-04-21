class MyIterator:

    def __init__(self, iterable, start, end, step):
        self.iterable = iterable
        self.start = start
        self.end = end
        self.step = step
        self.pointer = start

    def __iter__(self):
        return self
        # return MyIterator(self.iterable, self.start, self.end, self.step)
    
    def __next__(self):
        if self.pointer <= self.end:
            try:
                item = self.iterable[self.pointer]
                self.pointer += self.step
                return item
            except IndexError:
                raise StopIteration
        else:
            raise StopIteration

# list
# next(list)
# iter(list)
class MyIterable:

    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        return MyIterator(self.sequence, 0, len(self.sequence), 3)
        
#         0  1  2  3  4  5 
my_list =[1, 2, 3, 4, 5, 6 ,7 ,8] 
my_iterator = MyIterator(my_list, 1, 5, 2)
# iter(my_iterator)

print(next(my_iterator)) # 2 
print(next(my_iterator)) # 4

# my_iterator2 = iter(my_iterator)
# next(my_iterator2)
print("-----------------")
for item in my_iterator: 
    print(item)

print("-----------------")
# print(next(my_iterator))
# my_iterator = iter(my_iterator)
# my_iterator = MyIterable()

print("-----------------")

my_list = [1, 2, 3, 4, 5, 6, 7]
my_iterable = MyIterable(sequence=my_list)

        #   iter(my_iterable)
for item in my_iterable:
    print(item)

# TypeError: 'MyIterable' object is not an iterator
print(next(my_iterable))