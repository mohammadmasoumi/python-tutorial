def my_sort(n):
    return abs(n - 50)


a_list = [1, 10, 50, 60, 40]  # abs(n - 50)
# [(1, 49), (10, 40), (50 , 0), (60, 10), (40, 10)]
# [(50 , 0), (60, 10), (40, 10), (10, 40), (1, 49)]
# [50, 60, 40, 10, 1]

print(a_list)
a_list.sort(key=my_sort)
print(a_list)
