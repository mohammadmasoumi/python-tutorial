# lazy function
def my_iter(data):
    for item in data:
        yield item


def my_gen():
    yield 10
    yield 11
    yield 12


my_list = [1, 2, 3, 4]
iterator = my_iter(my_list)  # lazy function

print(type(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# for item in my_iter([1, 2, 3, 4]):
#     print(item)

gen = my_gen()

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))
