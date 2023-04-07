import time

my_list = [1, 2, 3, 4]


"""
item: 1, my_list = [1, 2, 3, 4]
item: 2, my_list = [1, 2, 3, 4, 1]
item: 3, my_list = [1, 2, 3, 4, 1, 2]
...
"""

for item in my_list:
    time.sleep(1)
    print(item, my_list)
    my_list.append(item)

print("Hello")