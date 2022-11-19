my_list = [1, 2, 3, 4, 5, 6]

# lambda (inputs):(output)
double = lambda x: x * 2
my_func1 = lambda x, y: x * y

print(double(2))
print(double(3))
print(my_func1(2, 3))
# print(my_func1(2,))
# def double(x):
#     return x * 2

print(map(double, my_list))
print(map(lambda item: item * 2, my_list))

def my_map(func, iterable):
    # func = a
    # func = 12

    # iterable = b
    # iterable = 13

    # func = lambda x: x * 2
    # iterable = my_list =  [1, 2, 3, 4, 5, 6]
    new_list = []
    for item in iterable:
        new_list.append(func(item))

    return new_list

def my_map2(a, b):
    new_list = []
    for item in b:
        new_list.append(     a(item)    )

    return new_list


# a = 12
# b = 13

# my_map(a, b)
# my_map(12, 13)

print(my_map(lambda x: x * 2, my_list))
print(my_map(lambda x: x * 2, [1, 2, 3 ,4]))
print(my_map2(lambda x: x // 2, [1, 2, 3 ,4]))