my_list = [1, 2, 3, 4]


for item in my_list:
    my_list.remove(item)

print(my_list)
print("----------------------------")

my_list = [1, 2, 3, 4]
index = 0
for item in my_list:
    my_list.pop(index)

print(my_list)
print("----------------------------")
my_list = [1, 2, 3, 4]


"""
my_list = [1, 2, 3, 4]
# my_list.copy() = [1, 2, 3, 4]
my_list2 = my_list.copy()

for item in my_list.copy():
    # item: 1, 
    my_list.remove(item) 

"""

for item in my_list.copy():
    my_list.remove(item)

print(my_list)
