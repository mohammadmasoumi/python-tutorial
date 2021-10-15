def my_sort(item):
    return abs(item - 50)
    # return item


a1 = [(1, 1), (10, 2), (50, 3), (60, 4), (40, 5)]


# do not do this
def my_sort2(item1):
    for item in a1:
        if item[0] == item1:
            return item[1]

    # return
    # return None
    # unreachable
    # print("Hello")


my_list = [1, 10, 50, 60, 40]  # abs(n - 50)
# [(1, 49), (10, 40), (50, 0), (60, 10), (40, 10)]
# now sort
# [(50, 0), (60, 10), (40, 10), (10, 40), (1, 49)]
# [50, 60, 40, 10, 1]

my_list2 = my_list.copy()
my_list2.sort(key=my_sort)

print(my_list)
print(my_list2)
