# High order function
# a function takes another function as an input params

# The map function applies a function to each member of a collection
def my_custom_map(func, iterable):
    return [func(item) for item in iterable]


def my_custom_filter(func, iterable):
    return [item for item in iterable if func(item)]


def multiply_by_2(item):
    return item * 2


def is_even(x):
    return x % 2 == 0


print(my_custom_map(multiply_by_2, range(5)))
print(my_custom_filter(is_even, range(5)))
print(my_custom_map(multiply_by_2, my_custom_filter(is_even, range(5))))
