# [19, 20, 18, 17, 10]
# +2

my_list = [20, 19, 18, 17, 10]

# 1. 
for idx in range(len(my_list)):
    if my_list[idx] < 18:
        my_list[idx] += 2
    else:
        my_list[idx] = 20

# 2.
# max(), min()
for idx in range(len(my_list)):
    # 0, 1, 2, 3,
    # WRONG len(idx)
    # item: my_list[idx]
    my_list[idx] = min(my_list[idx] + 2, 20)

