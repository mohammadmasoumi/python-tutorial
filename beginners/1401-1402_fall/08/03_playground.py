# 1.
# input
#                0            1
#            0     1        2     3
my_list = ["Ali", 19.7, "Hassan", 20]

# 0 -> 0 
# 1 -> 2
# y = 2 * x

# 0 -> 1 
# 1 -> 3
# y = 2 * x + 1

# output
# name: Ali | avg: 19.5
# name: Hassan | avg: 19.0

# range(len(my_list)//2)
# range(2)
# [0, 1]
# my_list = ["Ali", 19.7, "Hassan", 20]

for index in range(len(my_list)//2):
    # index = 0, name: my_list[0], avg: my_list[1] 
    # index = 1, name: my_list[2], avg: my_list[3]

    name = my_list[index*2]
    avg = my_list[index*2+1]

    print(f"Name: {name} | Avg: {avg}")

print("-" * 42)
# --------------------------------------------------------
# range(0, 4, 2)
# [0, 2]
#            0     1        2     3       4      5
my_list = ["Ali", 19.7, "Hassan", 20, "Asghar", 20]

print(f"{'Name': <20} | {'Avg': <20}")
print("-" * 42)
for index in range(0, len(my_list), 2):
    # index = 0, name: my_list[0], avg: my_list[1] 
    # index = 1, name: my_list[2], avg: my_list[3]

    name = my_list[index]
    avg = my_list[index+1]

    print(f"{name: <20} |  {avg: <20}")