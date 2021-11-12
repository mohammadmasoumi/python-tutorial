list1 = [10, 20, 30, 40]  # 0, 1, 2, 3
list2 = [100, 200, 300]  # 0, 1, 2: len(list2) -1
# 2 <= 2
# 2 < 3

for idx, item in enumerate(list1):
    # print(idx, item, len(list1))
    # if idx < len(list2):
    if idx < len(list2):
        print(list2[idx])
