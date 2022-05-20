n = input()


my_list = []

for character in n:

    for item in my_list:
        if item[0] == character:
            item[1] += 1
            break
    else:
        my_list.append([character, 1])


for char, value in my_list:
    print(f"{char}: {value}")