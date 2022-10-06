my_list = [1, 2, 3, 4 ,5]

# n rotates to right
n = int(input())
direction = input()
n = n % len(my_list)


# first solution

if direction == "right":
    print(my_list[-n:] + my_list[:-n])
else:
    print(my_list[n:] + my_list[:n])


# second solution

if direction == "right":
    for _ in range(n):
        # first remove item from the last
        item = my_list.pop()

        # then insert it at first
        my_list.insert(0, item)

        # or in one line
        # my_list.insert(0, my_list.pop())
else:
    for _ in range(n):

        # first remove item from the last
        item = my_list.pop(0)

        # then insert it at first
        my_list.append(item)


        # or in one line
        # my_list.append(my_list.pop(0))

print(my_list)