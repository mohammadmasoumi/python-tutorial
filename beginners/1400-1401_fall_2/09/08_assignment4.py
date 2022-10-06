"""
4
ali
name
hello
are
"""

a = int(input())

# my_list[a]
my_list = []

string = "*" * a
print(string)

# for item in :
# input()
# input()
# input()
# input()
# print(list(range(12)))  # [0, ... , 11]
# print(list(range(5)))  # [0, ... , 4]

# for idx in range(a):
#     my_list.append(input())

# for idx in string:
#     my_list.append(input())

for _ in string:
    my_list.append(input())

#
# print("#".join(my_list))
# print(my_list)
