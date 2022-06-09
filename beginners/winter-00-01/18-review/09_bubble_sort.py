my_list = [20, 5, 2, 1, 10, 12]

a = 12
b = 13
a, b = b, a

for idx1 in range(len(my_list)):
    for idx2 in range(len(my_list) - idx1 - 1):
        if my_list[idx2] < my_list[idx2 + 1]:
            my_list[idx2], my_list[idx2 + 1] = my_list[idx2 + 1], my_list[idx2]

print(my_list)

# --------------------------------
my_list = [20, 5, 2, 1, 10, 12]

a = 12
b = 13
a, b = b, a

for idx1 in range(len(my_list)):
    for idx2 in range(len(my_list) - idx1 - 1):
        if my_list[idx2] > my_list[idx2 + 1]:
            my_list[idx2], my_list[idx2 + 1] = my_list[idx2 + 1], my_list[idx2]

print(my_list)