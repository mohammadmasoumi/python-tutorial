my_list = [1, 2, 3, 4]

# index: 0, 1, 2
for item in my_list:
    # my_list: [1, 2, 3, 4]
    # item: my_list[0] => 1
    # my_list: [2, 3, 4]
    # item: my_list[1] => 3
    my_list.remove(item)
    # my_list: [2, 3, 4]
    # my_list: [2, 4]
    
print(my_list)
print("---------------------------------")

my_list = [1, 2, 3, 4]
my_list2 = my_list.copy() # [1, 2, 3, 4]

# my_list = [1, 2, 3, 4]
# my_list2 = my_list.copy() # [1, 2, 3, 4]

# index: 0, 1, 2
for item in my_list2:
    # my_list2: [1, 2, 3, 4]
    # my_list: [1, 2, 3, 4]
    # item: my_list2[0] => 1
    # -----------------------
    # my_list2: [1, 2, 3, 4]
    # my_list: [2, 3, 4]
    # item: my_list2[1] => 2
    # -----------------------
    # my_list2: [1, 2, 3, 4]
    # my_list: [3, 4]
    # item: my_list2[2] => 3
    my_list.remove(item)
    # my_list2: [1, 2, 3, 4]
    # my_list: [2, 3, 4]
    # -----------------------
    # my_list2: [1, 2, 3, 4]
    # my_list: [3, 4]
    # -----------------------
    # my_list2: [1, 2, 3, 4]
    # my_list: [4]
    
print(my_list)
print("---------------------------------")

my_list = [1, 2, 3, 4]
index = 0

# item = my_list.pop(0)
# item: 1
# item = my_list.pop()
# item: 4

# pointer: 0, 1
for item in my_list:
    # index: 0, item: 1 my_list[pointer: 0], my_list: [1, 2, 3, 4]
    # index: 0, item: 3 my_list[pointer: 1], my_list: [2, 3, 4]
    my_list.pop(index)
    # index: 0, item: 1, my_list: [2, 3, 4]
    # index: 0, item: 3, my_list: [3, 4]
    # index += 1

print(my_list)

print("---------------------------------")

# my_list = [1, 2, 3, 4]
# index = 0

# # pointer: 0, 1
# for item in my_list:
#     # index = 0, item: 1, my_list = [1, 2, 3, 4]
#     # index = 0, item: 4, my_list = [2, 4]

#     my_list.pop(index) # my_list = [2, 3, 4], my_list = [4]
#     my_list.pop(index+1) # my_list = [2, 4], IndexError: pop index out of range

# print(my_list)


print("---------------------------------")
my_list = [1, 2, 3, 4]
index = 0

# pointer: 0, 1
for item in my_list:
    # item: 1, my_list = [1, 2, 3, 4]
    # item: 4, my_list = [3, 4]
    my_list.pop(index)  # item: 1, my_list = [2, 3, 4], item: 4, my_list = [4]
    my_list.pop(index)  # item: 1, my_list = [3, 4], item: 4, my_list = []

print(my_list)

print("-----------------------------")
my_list = [1, 2, 3, 4]
index = 1

for item in my_list:
    my_list.pop(index)
    index += 1

print(my_list)
print("----------------------------")