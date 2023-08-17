my_list = [1, 2, 3, 4, 5, 4, 2, 1]

# 1. max
# idx[my_list]

curr_max = 0
curr_max = my_list[0]

for idx, item in enumerate(my_list):
    if item > curr_max:
        curr_max = item

print(curr_max)

# 2. second max 
curr_max = 0
curr_max = my_list[0]
second_max = my_list[0]

# 9 10 11 12
# my_list = [9 9 10 11 10.5]
# curr_max: 9|10|11
# second_max: 0|9|10|10.5

# if item > max
#   update max and second max
# if second max < item < max
#   update second max

# new second_max: old max

for idx, item in enumerate(my_list):
    if item > curr_max:
        second_max = curr_max
        curr_max = item
    elif second_max < item < curr_max:
        second_max = item

print(curr_max, second_max)