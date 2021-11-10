a_string1 = "first"
a_string2 = "first"

# unique identifier
print(id(a_string1))
print(id(a_string2))
print("--------------------------")

a_list1 = [1, 2]
a_list2 = [1, 2]

print(id(a_list1))
print(id(a_list2))

a_list3 = a_list1
print(id(a_list1))
print(id(a_list3))

a_list3.append(3)
print(a_list3)
print(a_list1)

print("--------------------------")

# int("1")
# float()

a_list4 = a_list1.copy()
a_list5 = list(a_list1)
print(id(a_list4))
print(id(a_list1))
print(id(a_list5))

a_list4.append(5)
a_list5.append(6)

print(a_list4)
print(a_list5)
