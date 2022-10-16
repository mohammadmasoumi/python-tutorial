my_list = [1, 2, 3, 4]

"""
my_list = [1, 2, 3, 4]

map(func, my_list)

new_my_list = []
for item in my_list:
    new_my_list.append(func(item))

"""
# map
def multiply_by_2(value):
    return value * 2

print(list(map(multiply_by_2 , my_list)))
print(list(map(lambda value: value*2, my_list)))
print(list(map(lambda item: item*2, my_list)))

new_list = []
for item in my_list:
    new_list.append(item * 2)
print(new_list)

# filter
my_list = [1, 2, 3, 4]
# new_my_list = []

# for item in my_list:
#     # item % 2 => (0, 1)
#     # if 0: => 0 == False
#     # if 1: => 1 == True

#     # if item % 2 == 1:
#     #     pass
#     if item % 2:
#         new_my_list.append(item)
# print(new_my_list)

def is_odd(value):
    # value: 1, True, 1
    # value: 2, False, 0
    return value % 2

print(list(filter(is_odd , my_list)))
print(list(filter(lambda value: value % 2 , my_list)))

