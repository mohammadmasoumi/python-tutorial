
#          0  1  2  3
my_list = [1, 2, 3, 10]

# method 1
acc = 0
counter = 0
for elem in my_list:
    acc += elem
    counter += 1

print(f"avg: {acc / counter}")

# method 2
# print(f"avg: {sum(my_list) / len(my_list)}")


# division
acc = my_list[0]

# my_list[1:] = [2, 3, 10]
for elem in my_list[1:]:
    acc /= elem

print(acc)