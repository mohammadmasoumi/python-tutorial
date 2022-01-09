#  HOTEL  [0]  [1]    [2]      [3]     [4]
my_list = [1, False, "Ali", [1, 2, 3], 10.2]

# update
# which room?   which value?
# حسن را داخل اتاق شماره 2 میریزیم
my_list[2] = "Hassan"

# multiply by 2
#           0  1  2  3  4
my_list2 = [1, 2, 3, 4, 5]

# print(my_list2[0])
# my_list2[0] = my_list2[0] * 2
# my_list2[1] = my_list2[1] * 2
# my_list2[2] = my_list2[2] * 2
# my_list2[3] = my_list2[3] * 2
# my_list2[4] = my_list2[4] * 2
#
# my_list2[0] *= 2
# my_list2[1] *= 2
# my_list2[2] *= 2
# my_list2[3] *= 2
# my_list2[4] *= 2

room_number = 0
for item in my_list2:
    my_list2[room_number] *= 2
    # my_list2[room_number] = item * 2
    # my_list2[room_number] = my_list2[room_number] * 2
