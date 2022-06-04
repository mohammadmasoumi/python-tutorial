my_list = [5, 20, 6, 10, 1, 2]


for rnd in range(len(my_list)):
    index = 0
    while index < len(my_list) - 1 - rnd:
        if my_list[index] > my_list[index + 1]:
            my_list[index], my_list[index + 1] = my_list[index + 1] , my_list[index]

        index += 1     

print(my_list)