iterable = [-10, 200, 3, 2]

def my_for(iterable):
    iterator = iter(iterable)
    # TypeError: object of type 'list_iterator' has no len()
    # print(len(iterator))
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

my_for(iterable=iterable)

for item in iterable:
    print(item)