my_list = [1, 0, 0, 0, 0, 2, 3, 10, 0, 0, 0, 9, 10, 20, 30, 0]
# my_list = [1, 2, 3, 10, 9, 0, 0, 0,]

# 1
# [1, 0, 0, 2, 3, 10, 0, 0, 0, 9]
# [1, 0, 2, 3, 10, 0, 0, 0, 9, 0]
# [1, 2, 3, 10, 0, 0, 0, 9, 0, 0,]


# for item in my_list:
#     if item == 0:
#         # print(f"my_list{my_list}, item: {item}")
#         my_list.remove(item)
#         my_list.append(0)

# 2
# copied_list = my_list.copy()
# for idx, item in enumerate(my_list):
#     if item == 0:
#         m = copied_list.pop(idx)
#         copied_list.append(m)
#
# # [1, 2, 3, 10, 9, 0, 0, 0]
# print(copied_list)


# 3
# my_list = [1, 0, 0, 2, 3, 10, 0, 0, 0, 9]
# my_zeros = []
# copied_list = my_list.copy()
# for item in my_list:
#     if item == 0:
#         copied_list.remove(item)
#         my_zeros.append(0)
#
# # my_list + my_zeros
# # my_zeros.extend(my_list) Wrong
# copied_list.extend(my_zeros)

# print(my_list)
# print(copied_list)

# 4
# [1, 0, 0, 2, 3, 10, 0, 0, 0, 9]
# index = 0
# len = len(my_list)
# while index < len:
#     # if index == 0:
#     print(f"[BEFORE]: index: {index}, my_list: {my_list}")
#
#     item = my_list[index]
#     if item == 0:
#         # اولین صفری که ببینه رو پاک میکنه
#         my_list.remove(item)
#         my_list.append(0)
#
#     print(f"[AFTER]: index: {index}, my_list: {my_list}")
#     print("-------------------------------------------")
#     index += 1

# 5
index = 0
len = len(my_list)
count_zero = my_list.count(0)

while index < len:
    # if index == 0:
    print(f"[BEFORE]: index: {index}, my_list: {my_list}")

    item = my_list[index]
    if item == 0:
        # اولین صفری که ببینه رو پاک میکنه
        my_list.pop(index)
        my_list.append(0)
        if index == len - count_zero:
            break
    else:
        print(f"[AFTER]: index: {index}, my_list: {my_list}")
        print("-------------------------------------------")
        index += 1

print(my_list)
