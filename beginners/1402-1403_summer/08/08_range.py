my_list = [1, 2, 3, 4]

# slicing
# start: included
# end: not included
# step: -/+
# my_list[start:end:step]
# my_list[:3]

# range(start:end:step)
# range(3): [0, 1, 2]
# range(1, 3): [1, 2]

for item in my_list:
    print(item)


# my_list: [1, 2, 3, 4]
# range(len(my_list)): [0, 1, 2, 3]
for idx in range(len(my_list)):
    # item: my_list[idx]
    # idx: 0, item: 1
    my_list[idx] += 10


my_list = [1, 2, 3]
print(my_list[0]) # access
my_list[0] = 10 # update
del my_list[0] # delete