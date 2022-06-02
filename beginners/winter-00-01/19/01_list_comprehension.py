# 
my_list = [1, 2, 3, 4, 5]

for idx in range(len(my_list)):
    if my_list[idx] % 2 == 0:
        my_list[idx] //= 2
    else:
        my_list[idx] *= 2

# print(my_list)

#
my_list = [1, 2, 3, 4, 5]

# a = 3
# [ item*2     for item in iterable ]
# [ item//2     for item in iterable ]
# [ item*a     for item in iterable ]
# create a new list

my_list = [item*2 for item in my_list]
my_list2 = [       item*2 for item in my_list         ]

print(my_list)
print([item*2 for item in my_list])
print([item//2 for item in my_list])
print(my_list)
