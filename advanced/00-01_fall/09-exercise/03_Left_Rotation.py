len_arr, left_rotate = map(int, input().split())
arr = input().split()
left_rotate = left_rotate % len_arr
print(' '.join(arr[left_rotate:] + arr[: left_rotate]))
