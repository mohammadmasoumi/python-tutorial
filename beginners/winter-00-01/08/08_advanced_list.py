my_list = [12, 13, 14]

print(id(my_list))
print(id(my_list[0]), id(my_list[1]), id(my_list[2]))
print(id(my_list[1]) - id(my_list[0]))
print(id(my_list[2]) - id(my_list[1]))
print("--------------------")

my_list.append(15)
print(id(my_list[1]) - id(my_list[0]))
print(id(my_list[2]) - id(my_list[1]))
print(id(my_list[3]) - id(my_list[2]))
print("--------------------")

my_list.remove(13)
print(id(my_list[1]) - id(my_list[0]))
print(id(my_list[2]) - id(my_list[1]))
print("--------------------")

my_list.insert(1, 16)
print(id(my_list[1]) - id(my_list[0]))
print(id(my_list[2]) - id(my_list[1]))
print(id(my_list[3]) - id(my_list[2]))