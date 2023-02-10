# Identity operator

a = 12
# b = a 
b = 12
c = [12]

d = "Ali"
e = "Ali"

"""
id 
"""

print(id(a))
print(id(b))
print(id(c[0]))

print(id(d))
print(id(e))

print(id(d) == id(e))
print(d is e) # d and e are the same object

print("-------------------")

# mutable
my_list1 = [1, 2]
my_list2 = [1, 2]

print(id(my_list1))
print(id(my_list2))

print(my_list1 == my_list2) # Value

# print(id(my_list1) == id(my_list2))
print(my_list1 is my_list2) # Identity

print("-------------------")

# mutable
my_list1 = [1, 2]
my_list2 = my_list1

print(id(my_list1))
print(id(my_list2))

print(my_list1 == my_list2) # Value

# print(id(my_list1) == id(my_list2))
print(my_list1 is my_list2) # Identity

print("-------------------")

# mutable
my_list1 = [1, 2]
my_list2 = my_list1.copy()

print(id(my_list1))
print(id(my_list2))

print(my_list1 == my_list2) # Value

# print(id(my_list1) == id(my_list2))
print(my_list1 is my_list2) # Identity