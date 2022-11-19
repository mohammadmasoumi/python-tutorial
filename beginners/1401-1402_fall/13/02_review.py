my_list = [1, 2, 3, 4]

# list comprehension
print([item for item in my_list])
print([item * 2 for item in my_list])
print([item * 2 for item in my_list if item % 2])
print([item // 2 for item in my_list if not (item % 2)])

my_list2 = [item // 2 for item in my_list if not (item % 2)]

# if (condition)
# result_true if (condition) else result_false
print([item // 2 if not (item % 2) else item * item for item in my_list])

my_list = [[1, 2, 3], [4, 5, 6]]

print([item for items in my_list for item in items])
print([item for items in my_list for item in items if item % 2])
print([item * 2 if item % 2 else item // 2 for items in my_list for item in items])

my_list = [1, 2, 3, 4]

def function(x):
    return x % 2

#             function  iterable
print([          filter(function, my_list)       ])
a = list(filter(function, my_list))
print(a)

# built-in
b = filter(function, my_list)
print(list(filter(function, my_list)))

for item in b:
    print(item)

print("--------------")
print(b)
for item in b:
    print(item)


# my_new_list = []

# for item in my_list:
#     if function(item):
#         my_new_list.append(item)
