def insertion_sort(arr):
    for i in range(len(arr)):

        min_key = 10000
        min_index = -1
        for j in range(i, len(arr)):
            if arr[j] < min_key:
                min_key = arr[j]
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


my_list = [50, 20, 30, 40, 10, 80, 5]
insertion_sort(my_list)

print(my_list)
