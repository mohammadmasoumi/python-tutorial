my_list = []

# False values
print(bool(my_list))
print(bool(0))
print(bool(""))
# print(bool(my_list[0]))
# if bool(my_list):
# if bool(my_list):
if bool(my_list):
    print("empty list")

# IndexError: list index out of range
# print(my_list[0])
if my_list and my_list[0]:
    print("You hooo")

my_list2 = [1, 2, 3, 4]
# my_list2[1:3] = [10]
# my_list2[1:3] = [10, 11]
my_list2[1:3] = [10, 11, 12]
print(my_list2)

my_list3 = [1, 2, [3, 4]]
print(3 in my_list3)
print(2 in my_list3)
print(2 in my_list3[2])
