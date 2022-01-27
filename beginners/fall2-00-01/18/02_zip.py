# 
# zip - buiilt-in function
# ignore  "nationality"
my_list1 = ["name", "last_name", "city", "nationality"]
my_list2 = ["asghar", "asghari", "varamin", ]

print(zip(my_list1, my_list2))
# [('name', 'asghar'), ('last_name', 'asghari'), ('city', 'varamin')]
print(list(zip(my_list1, my_list2)))
# {'name': 'asghar', 'last_name': 'asghari', 'city': 'varamin'}       
print(dict(zip(my_list1, my_list2)))

print(dict([("a", 1), ("b", 2)]))