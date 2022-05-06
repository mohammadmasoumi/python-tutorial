my_list = [1, 2, 3, 4 ,5 ]
n = int(input())
n = n % len(my_list) # 11 = 5 = 1

# print(my_list[:1] + my_list[1:])
# print(my_list[:2] + my_list[2:])
# print(my_list[:3] + my_list[3:])
# print(my_list[:4] + my_list[4:])
# print(my_list[:0] + my_list[0:])

print(my_list[:n] + my_list[n:])