n = int(input())
my_list = []

"""
# 1.
my_list = ["Ali", 19.7, "Hassan", 20]

name: Ali | avg: 19.5
name: Hassan | avg: 19.0

# range(0, 4, 2)
# [0, 2]

# range(len(my_list)//2)
# range(2)
# [0, 1]
# my_list = ["Ali", 19.7, "Hassan", 20]

for index in range(len(my_list)//2):
    # index = 0, name: my_list[0], avg: my_list[1] 
    # index = 1, name: my_list[2], avg: my_list[3]
    

    name = my_list[idnex*2]
    avg = my_list[idnex*2+1]

for index in range(0, len(my_list), 2):

# 2.
# my_list = [["Ali", 19.7], ["Hassan", 20]]


"""

for _ in range(n):
    items = input().split()

    # input()
    # input()

    # 1. Human way
    # items = ['asghar', '20', '20']
    # items = ['20', '20']
    # name = "asghar"
    name = items.pop(0)

    s = 0
    for item in items:
        s += int(item)

    # 2. The monkey way
    # s = 0
    # name = ""
    # for item in items:
    #     if item.isdigit():
    #         s += int(item)
    #     else:
    #         name = item

    # my_list = ["Ali", 19.7, "Hassan", 20]
    avg = s / len(items)
    # my_list.extend([name, avg])

    # first way
    # my_list.append(name)
    # my_list.append(avg)
    # print(f"name: {name} | avg: {s / len(items)}")

    # second way
    
    my_list.append([name, avg])

# print(my_list)
# first way
# for index in range(0, len(my_list), 2):
#     name = my_list[index]
#     avg = my_list[index+1]
#     print(f"name: {name} | avg: {avg}")

# second way
# my_list = [["Ali", 19.7], ["Hassan", 20]]
for name, avg in my_list:
    print(f"name: {name} | avg: {avg}")