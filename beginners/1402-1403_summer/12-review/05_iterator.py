# iterator

# iterable
# capable of iteration

# iterator
# you can iterate over it

# iterable -> iterator


my_list = [1, 2, 3, 4] # iterable
iterator = iter(my_list) # iterator

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # StopIteration

# iterator: iter(my_list)
# item: next(iterator)
for item in my_list:
    print(item)

# 
def for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            yield next(iterator)
        except StopIteration:
            break


my_list = [1, 2, 3, 4, 5]
for item in for_loop(my_list):
    print(item)