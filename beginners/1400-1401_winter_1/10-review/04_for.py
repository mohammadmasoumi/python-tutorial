
"""
Iterable:
چیزی که من میتوانم روی آن بچرخم

# background
#   index

for item/element/character/elem/idx in Iterable:
    print(item) 
"""
# remove

my_list = [1, 2, 3, 4]

# index: 0,  my_list: [1, 2, 3, 4]  
# index: 1,  my_list: [2, 3, 4]  
# index: 2,  my_list: [2, 4]  ?? => END OF LOOP
for item in my_list:
    # [1] item: 1, index: 0, my_list: [1, 2, 3, 4]  
    # [2] item: 3, index: 1, my_list: [2, 3, 4]  
    print(item)
    my_list.remove(item)
    # [1] item: 1, index: 0, my_list: [2, 3, 4]  
    # [2] item: 3, index: 1, my_list: [2, 4]  

# terminal 
# 1
# 3 

# append - unlimited loop
my_list = [1, 2, 3, 4]

for item in my_list:
    # item: 1, my_list: [1, 2, 3, 4] 
    # item: 2, my_list: [1, 2, 3, 4, 1] 
    # item: 3, my_list: [1, 2, 3, 4, 1, 2] 
    # item: 4, my_list: [1, 2, 3, 4, 1, 2, 3] 
    print(my_list)
    my_list.append(item)
    # item: 1, my_list: [1, 2, 3, 4, 1] 
    # item: 2, my_list: [1, 2, 3, 4, 1, 2] 
    # item: 3, my_list: [1, 2, 3, 4, 1, 2, 3] 
    # item: 4, my_list: [1, 2, 3, 4, 1, 2, 3, 4]

