# iterator ->  next()
# iterable -> iter()

# iterable -> iterator

def my_for(iterable):
    iterator = iter(iterable)
    
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


# iterable
my_list = [1, 2, 3, 4]
# my_for()

# TypeError: 'list' object is not an iterator
# print(next(my_list))

# Iterator
# my_iter = iter(my_list) 
# print(next(my_iter))

