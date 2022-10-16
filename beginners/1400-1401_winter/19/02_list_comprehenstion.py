#
my_list = [1, 2, 3, 4, 5]

# value % 2 -> [0, 1]

# if value % 2: == if 1:
#   فرد

# if not (value % 2):
# if value % 2 == 0:
# زوج

my_list2 = [item*2 for item in my_list if item % 2]
my_list3 = [value*2 for value in my_list if value % 2]

#                            inline if-else
# my_list3 = [(      (value*2) if (value % 2) else (value // 2)    ) for value in my_list]

my_list3 = [value*2 if value % 2 else value // 2 for value in my_list]

print(my_list2)
print(my_list3)
