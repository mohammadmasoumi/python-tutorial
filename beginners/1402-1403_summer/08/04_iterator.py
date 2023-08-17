iterable = [1, 2, 3]
# TypeError: 'list' object is not an iterator
# print(next(iterable))

iterator = iter(iterable)

print(next(iterator))  # index: 0
print(next(iterator))  # index: 1
print(next(iterator))  # index: 2
print(next(iterator))  # StopIteration

while True:
    try:
        print(next(iterator))
    except StopIteration:
        pass
