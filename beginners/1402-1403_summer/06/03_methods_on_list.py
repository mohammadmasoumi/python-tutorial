# methods on list

my_list = [1, 2, 3, 4, 5, 6]

# append
# append an item to the end of the list
my_list.append(7)

print(my_list)
print(my_list.append(8)) # None
print(my_list)

# print(int("12"))

# extend
my_list.extend([9, 10, 11])
my_list.append([9, 10, 11])
print(my_list)

print("-------------")
my_list1 = [1, 2, 3]
my_list1.append([4, 5])
print(my_list1)
my_list1.extend([4, 5])
print(my_list1)

print("-------------")
my_names = ["ali", "reza"]
my_names.append("karkabadi")
# ["k", "a", "v", ...]
my_names.extend("karkabadi") # iterable
print(my_names)
print("-------------")

# remove
# remove from the left side
students = ["karkabadi", "karkabadi", "amiri", "safari"]
students.remove("karkabadi")
print(students)
# ValueError: list.remove(x): x not in list
#               item
# students.remove("x")
# students.remove("a")



