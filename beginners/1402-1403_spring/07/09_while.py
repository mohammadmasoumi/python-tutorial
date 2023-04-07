#          0        3
my_list = [1, 2, 3, 4]

"""
while CONDITION:
    BODY

"""
idx = 0

while idx < len(my_list): # len(my_list): 4
    print(my_list[idx]) # my_list[0],  my_list[1], my_list[2], my_list[3]
    idx += 1 # idx: 1, 2, 3, 4


print("-----------------------------")
idx = 0

while True:
    if idx >= len(my_list):
        break

    print(my_list[idx])
    idx += 1

print("-----------------------------")
idx = 0

while True:
    print(my_list[idx]) # my_list[0], my_list[1], my_list[2], my_list[3] 
    idx += 1 # idx: 1, idx: 2, idx: 3, idx: 4

    if idx >= len(my_list): # 1 >= 4 X, 2 >= 4 , 3 >= 4, 4 >= 4
        break

