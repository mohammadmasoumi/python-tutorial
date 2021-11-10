my_list = [1, 2, 3, 4]

for idx, addad in enumerate(my_list):
    addad += 1
    print(idx, addad)
    my_list[idx] = addad

print(my_list)
