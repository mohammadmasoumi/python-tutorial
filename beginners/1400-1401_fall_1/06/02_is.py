# is operator

a_list1 = [1, 2]
a_list2 = [1, 2]
a_list3 = a_list2

print(id(a_list1))
print(id(a_list2))
print(id(a_list3))

# comparison
# print(id(a_list1) == id(a_list2))
print(a_list1 is a_list2)  # False
print(a_list1 == a_list2)  # True

# if `is`(keyword) is True => == must be True
print(a_list2 is a_list3)  # True
print(a_list2 == a_list3)  # True

print("---------------------")
# immutable
a = 'a'
b = 'a'

print(a is b)  # True
print(a == b)  # True
