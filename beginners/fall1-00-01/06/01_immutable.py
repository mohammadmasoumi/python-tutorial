# immutable
str1 = "mohammad"
str2 = "mohammad"
str3 = "Mohammad"

print(id(str1))
print(id(str2))
print(id(str3))

print("------------------------------")
# mutable
a_list1 = [1, 2]
a_list2 = [1, 2]

# put a_list3 label on box of a_list1
a_list3 = a_list1


# create another box and copy the value of a_list1 box into it
a_list4 = a_list1.copy()
# or a_list4 = list(a_list1)

print(id(a_list1))

print(id(a_list3))
print(id(a_list2))

a_list1.append(3)
print(a_list1)
print(a_list3)
