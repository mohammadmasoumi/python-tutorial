
"""
iterable C iterator

iterable -> list 
iterator

"""

my_list = [1, 2, 3, 4] # iterable
my_string = "hello"
# TypeError: 'list' object is not an iterator
# print(next(my_list))

# TypeError: 'str' object is not an iterator
# print(next(my_string))

list_iterator = iter(my_list)
str_iterator = iter(my_string)

print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
# print(next(list_iterator)) # StopIteration

# <class 'list_iterator'>
print(type(list_iterator))
# <class 'str_iterator'>
print(type(str_iterator))


def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            yield next(iterator)
        except StopIteration:
            break

my_list = [1, 2, 3, 4]
# for item in my_for(my_list):
#     print(item)

def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

my_for(my_list)