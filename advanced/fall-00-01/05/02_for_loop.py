# each element of list is list
# a_list2[0] = [1, 2]
# a_list2[1] = [3, 4]
a_list2 = [[1, 2], [3, 4]]

# a_list2 = [1, 2, 3, 4]
# a_list2.append(20)
# 1.append(2)

for item in a_list2:
    print(item. item[0], item[1])
    item.append(20)

for item in a_list2:
    print(item)

# change immutable elements
a_list = ["apple", "orange", "peach"]

# immnutable
a_string = "string"
a_string = a_string + "Hello"

a_list3 = []
a_list3.append(3)
# a_list3 = a_list3 + [3]

counter = 0
for fruit in a_list:
    print(fruit)
    fruit = fruit + "Hello"
    a_list[counter] = fruit
    counter += 1

for idx in range(len(a_list)):
    a_list[idx] = a_list[idx] + "Hello"
    # a_list[idx] += "Hello"

