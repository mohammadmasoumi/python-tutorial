my_list = [1, 2, 3, 4, 5]
n, direction = input().split()

n = int(n) % len(my_list)
counter = 0

if direction == "RIGHT":
    while counter < n:
        item = my_list.pop(-1)
        my_list.insert(0, item)
        counter += 1
elif direction == "LEFT":
    while counter < n:
        item = my_list.pop(0)
        my_list.append(item)
        counter += 1


print(my_list)