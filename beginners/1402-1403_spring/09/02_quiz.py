
my_list = [[10, 20, 30], [50, 40], 20, 30, 40]

"""
1. for loop

item
    list -> max + 1 replace with old max [mutable]
    int -> item + 1 replace with item [immutable] idx

"""
idx = 0
for item in my_list:
    if isinstance(item, list):
        # item: [10, 20, 30]
        max_item = max(item) # max_item: 30
        max_item_idx = item.index(max_item) # max_item_idx: 2
        item[max_item_idx] = max_item + 1 # item[2]  = 31
    elif isinstance(item, int):
        my_list[idx] = item + 1

    idx += 1

print(my_list)