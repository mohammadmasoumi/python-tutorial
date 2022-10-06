my_list = [12, 19, 6, 1, 5, 10]

for i in range(len(my_list)):
    for j in range(0, len(my_list) - 1 - i):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print(my_list)