# enumerate

# index      0       1         2         3
my_list = ["ali", "mobin", "hassan", "hossein"]

# update
# no update & no replace 
# my_list[0] = "asghar"

# builtin enumerate

# my_l = [1, 2, 3]
# a, b, c = my_l 
# print(f"a: {a}, b: {b}, c: {c}")

for item in enumerate(my_list):
    print(item)


print("---------------------------")
for item in enumerate(my_list):
    # idx, elem = (0, 'ali')
    # idx, elem = (1, 'mobin')
    # idx, elem = (2, 'hassan')
    # idx, elem = (3, 'hossein')
    # print(item)
    # unpacking
    idx, elem = item
    print(f"idx: {idx}, elem: {elem}, item: {item}")


print("---------------------------")
for idx, elem in enumerate(my_list):
    print(f"idx: {idx}, elem: {elem}")


# Usage ?
# 1. update an elemnt of the list
# 2. you wanna do sth with index

print("---------------------------")
index = 0
for elem in my_list:
    print(f"elem: {elem}, elem: {my_list[index]}, idx: {index}")
    index += 1

print("---------------------------")
for elem in my_list:
    print(f"elem: {elem}, idx: {my_list.index(elem)}")




# (3, 'hossein')
# print the last element of the list
# print(item)
# print(my_list)