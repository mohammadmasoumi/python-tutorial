# range

"""
range(start, end, step)

start: included
end: not included
step: step

create sequence of numbers
"""

#               end
print(list(range(10))) # [0, ..., 9]
#               start end
print(list(range(0, 100)))
#               start end step
print(list(range(0, 10, 2)))
print(list(range(0, 10, 3)))

# wrong syntax
# print(list(range(, 10, 3)))
# print(list(range(0, , 3)))
print(list(range(0, 3)))

print(range(0, 3)) # generator

my_range = range(0, 3) # range is iterable
# print(next(my_range))

for item in range(0, 3): # iterable -> iterator
    print(item)

# for create list indexes

my_list = [1, 2, 3, 4, 5]
for idx in range(len(my_list)): # 0 -> len-1
    print(idx)

# len
print(len(my_list))
# positive index -> [0, len-1]
# negative index -> [-len:-1]

#          0  1  2  3 -> [0: len-1]
#         -4 -3 -2 -1 
my_list = [1, 2, 3, 4]

# when index is needed?
# update values in the list

my_scores = [18, 17, 15, 12]
for score in my_scores:
    # access: score
    score += 2

for idx in range(len(my_scores)):
    # access: my_scores[idx]
    # update: my_scores[idx] += 2
    # delete: my_scores[idx] it might be wrong
    my_scores[idx] += 2

print(my_scores)


# list
my_list = [1, 2, 3, 4]

# 1. access
# access via index
print(my_list[0])
print(my_list[1])

# 2. update
# assign new values to the specific index
my_list[1] = 12
my_list[2] += 10

# 3. delete
# delete an item via index
del my_list[3]
