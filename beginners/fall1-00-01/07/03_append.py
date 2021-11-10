from time import sleep

my_list = list(range(10))

# print(list(my_list))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0]
for item in my_list:
    print(f"item: {item} len: {len(my_list)} my_list: {my_list}")
    my_list.append(item)
    sleep(10)
