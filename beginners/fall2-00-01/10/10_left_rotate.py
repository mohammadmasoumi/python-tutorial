my_list = [1, 2, 3, 4 ,5]

# n rotates to right
n = int(input())
n = n % len(my_list)


# first solution

# n=1 =>  [2, 3, 4, 5] + [1]
# n=2 =>  [3, 4, 5] + [1, 2]
# n=3 =>  [4, 5] + [1, 2, 3]
# n=4 =>  [5] + [1, 2, 3, 4]
# n=5 =>  [] + [1, 2, 3, 4, 5]
# ...
print(my_list[n:] + my_list[:n])


# second solution

# naming variable to _ means that the variable does not matter to us and we do not need it.
for _ in range(n):

    # first remove item from the last
    item = my_list.pop(0)

    # then insert it at first
    my_list.append(item)


    # or in one line
    # my_list.append(my_list.pop(0))

print(my_list)