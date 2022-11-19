my_list = [1, 2, 3, 4]

def evens(x):
    return not (x % 2)

def double(x):
    return x * 2

# a = filter(evens, my_list)
# b = map(double, a)
# print(list(b))

print(list(map(double, filter(evens, my_list))))
print([item * 2 for item in my_list if not (item % 2)])