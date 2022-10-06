# list

from black import mypyc_attr


my_list = ["ali", "mobina", "ali", "hassan", "ali", "hossein", "maryam", "mobina"]

# append(item)
my_list.append("mobin")

# pop(index)
item1 = my_list.pop()
itme2 = my_list.pop(0)

# remove(item)
my_list.remove("ali")

# index(item)
my_list.index("ali")

# extend(iterable)
my_list.extend([1, 2, 3])

# insert(index, item)
my_list.insert(2, "mahtab")

print(my_list)