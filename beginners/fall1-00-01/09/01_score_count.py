"""
12 20 20 12 11
[['12', 2], ['20', 2], ['11', 1]]
"""
# ['12', '20', '20', '11', '12']
scores = input().split()

# [[score1, count1], [score2, count2]]
# [['20', 2], ['12', 2], ['11', 1]]
# [['20', 3], ['12', 2], ['11', 1]]
my_list = []

# ['12', '20', '20', '11', '12']
for item in scores:

    # item = '12'
    # 1 من آیتم فعلی را قبلا دیده ام حال باید تعداد تکرار آن را یک مورد اضافه کنم
    # my_list = [['12', 1]]
    # my_list = [['12', 2]]
    # my_list = [['12', 1], ['12', 1]] مقدار ضحیح نمیباشد
    for idx, hasan_kachal in enumerate(my_list):
        # idx 0
        # items[0] 12 score
        # items[1] 1 count
        # unpack
        # a, b = [1, 2]
        # a = 1
        # b =2
        # items = ['12', 1]
        # mark, count = ['12', 1]
        # mark = '12'
        # count = 1
        mark, count = hasan_kachal

        if mark == item:
            count += 1
            # my_list[idx] = [mark, count]
            my_list[idx] = [item, count]
            break
    else:
        my_list.append([item, 1])

    # 2 من برای اولین با این عدد را دیده ام.
    # my_list = [['11', 1]]
    # my_list = [['11', 1], ['12', 1]]

print(my_list)

# select All: ctrl + a
# pretty: ctrl + alt + l
