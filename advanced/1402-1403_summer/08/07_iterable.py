# Iterator
iterable = [1, 2, 3, 4]

# TypeError: 'list' object is not an iterator
# print(next(iterable))
# iterable.__iter__
iterator = iter(iterable)

# built-in function
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # StopIteration

# def next(iterator):
#   return iterator.__next__()

# dunder method or magic function
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())