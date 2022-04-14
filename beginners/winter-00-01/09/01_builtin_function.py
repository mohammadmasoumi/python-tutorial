# built-in fuction

my_list = [1, 2, 3, 4]
my_list2 = ["ali", "hassan", "amir", "maryam"]
my_list3 = ["ali", 2]
my_list4 = [True, 2] # int(True) = 1
my_list5 = [True, 2.2]

# max
print(f"max(my_list): {max(my_list)}")
print(f"max(my_list2): {max(my_list2)}")
# TypeError: '>' not supported between instances of 'int' and 'str'
# print(f"max(my_list3): {max(my_list3)}")

# min
print(f"min(my_list): {min(my_list)}")
print(f"min(my_list2): {min(my_list2)}")

# sum
print(f"sum(my_list): {sum(my_list)}")
# sum([1, 2]) => 1 + 2
print(f"sum(my_list4): {sum(my_list4)}")
print(f"sum(my_list5): {sum(my_list5)}")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(f"sum(my_list2): {sum(my_list2)}")

# len
print(f"len: {len(my_list)}")

# all, any
# if all of them are True, I will return True
print(all([True, 12, 0, " "])) 
print(all([True, 12, 1, ""]))
print(all("ali", "mohammad", "amir", "")) # bool("") = False
# bool("") => False

# if one of them is True, I will return True
print(any([True, 12, 0, " "]))
print(any([False, "", 0])) 

