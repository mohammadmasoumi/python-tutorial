my_list = [1, 2, 3, 4 ,5 ]
n = int(input())
n = n % len(my_list) # 11 = 5 = 1

for _ in range(n):
    item = my_list.pop(0)
    my_list.append(item)

print(my_list)